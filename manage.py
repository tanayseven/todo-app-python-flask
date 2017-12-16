# -*- coding: utf-8 -*-
import os

from manager import Manager

manager = Manager()


@manager.command
def test():
    os.system(
        'pytest'
    )


@manager.command
def serve():
    os.system(
        'export FLASK_APP=todo_app.application;'
        'python -m flask run'
    )
