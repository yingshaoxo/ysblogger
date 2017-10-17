import os
import json

import markdown


class Updater():
    def __init__(self):
        # First, you should have a article dir under this path of __file__
        self.root = os.path.dirname(__file__)
        self.dir = os.path.join(self.root, 'article')
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    def get_changed(self):
        self.update_info()
        self.read_info()
        self.check_if_changed()
        return self.changed

    def update_info(self):
        self.new_files_with_date = dict([(os.path.join(self.dir, name), os.path.getmtime(os.path.join(self.dir, name))) for name in os.listdir(self.dir) if name[-3:] == '.md'])

    def save_info(self):
        with open(os.path.join(self.dir, 'setting.json'), mode='w') as f:
            f.write(json.dumps(self.new_files_with_date))

    def read_info(self):
        try:
            with open(os.path.join(self.dir, 'setting.json'), mode='r') as f:
                content = f.read()
            self.old_files_with_date = json.loads(content)
        except Exception as e:
            print(e)
            self.old_files_with_date = {}

    def check_if_changed(self):
        new = dict()
        self.changed = list()
        for name, time in self.new_files_with_date.items():
            new.update({name: time})
            old_time = self.old_files_with_date.get(name)
            if old_time: # file exsist in old_setting
                if time > old_time:
                    self.changed.append(name)
            else: # file do not exsist in old_setting
                self.changed.append(name)
        self.new_files_with_date = new
        self.save_info()


class Generater():
    def __init__(self):
        self.root = os.path.dirname(__file__)
        self.mddir = os.path.join(self.root, 'article')
        self.postdir = os.path.join(self.root, 'post')
        if not os.path.exists(self.mddir):
            os.mkdir(self.mddir)
        if not os.path.exists(self.postdir):
            os.mkdir(self.postdir)

    def generate(self, file_list):
        for name in file_list:
            name = os.path.basename(name)
            html = markdown.markdown(self.read_md(name), output_format='html5')
            self.write_html(name[:-3] + '.html', html)
    
    def read_md(self, name):
        with open(os.path.join(self.mddir, name), mode='r') as f:
            text = f.read()
        return text
        
    def write_html(self, name, html):
        with open(os.path.join(self.postdir, name), mode='w') as f:
            f.write(html)
        
        


u = Updater()
g = Generater()
need_to_change = u.get_changed()
print(need_to_change)
g.generate(need_to_change)
print('ok')
