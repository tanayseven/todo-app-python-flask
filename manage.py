# -*- coding: utf-8 -*-
import os

from manager import Manager

manager = Manager()


@manager.command
def echo(text=''):
    print(text)


@manager.command
def serve():
    os.system(
        'export FLASK_APP=todo_app.application;'
        'python -m flask run'
    )
