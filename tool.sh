#!/bin/bash

run() {
    python3.6 generater.py
}

pull() {
    git fetch --all
    git reset --hard origin/master
}

push() {
    git add .
    git commit -m "update"
    git push origin
}

if [ "$1" == "run" ]; then
    run

elif [ "$1" == "pull" ]; then
    pull

elif [ "$1" == "push" ]; then
    push

elif [ "$1" == "" ]; then
    echo "run 
pull
push"

fi
