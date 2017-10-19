import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from todo_app.admin.views import register_admin
from todo_app.extensions import app

register_admin(app)
manager = Manager(app)

print("*** CURRENT ENVIRONMENT: " + os.environ['TODO_APP'] + " ***")


@app.route('/something')
def something():
    return "Something is working"


@manager.command
def serve(host='0.0.0.0', port=5000, debug=False):
    app.run(host, port, debug=debug)


@manager.command
def test():
    pass


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
