import os
import json

class Updater():
    def __init__(self):
        # First, you should have a article dir under this path of __file__
        self.dir = os.path.join(os.path.dirname(__file__), 'article')

    def get_changed(self)
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
            self.save_info()

    def check_if_changed(self):
        new = dict()
        changed = list()
        for name, time in self.new_files_with_date.items():
            new.update({name: time})
            old_time = self.old_files_with_date.get(name)
            if old_time: # file exsist in old_setting
                if time > old_time:
                    changed.append(name)
            else: # file do not exsist in old_setting
                changed.append(name)
        self.changed = [os.path.join(self.dir, name) for name in changed]
        self.new_files_with_date = new
        self.save_info()


class generater():
    pass


u = Updater()
print(u.changed)
