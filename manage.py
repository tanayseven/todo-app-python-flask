# -*- coding: utf-8 -*-
import os

from manager import Manager

manager = Manager()


@manager.command
def test(filter='', capture=False):
    os.system(
        'pytest -k ' + filter + (' -s' if capture else '')
    )


@manager.command
def serve():
    os.system(
        'export FLASK_APP=todo_app.application;'
        'python -m flask run'
    )
