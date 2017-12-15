import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from todo_app.admin.views import register_admin
from todo_app.extensions import app
from todo_app.register import register_all_routes

register_admin(app)
manager = Manager(app)

env = os.environ.get('TODO_APP') or 'test'
print("*** CURRENT ENVIRONMENT: " + env + " ***")


@app.route('/something')
def something():
    return "Something is working"


@manager.command
def serve(host='0.0.0.0', port=5000, debug=False):
    register_all_routes()
    app.run(host, port, debug=debug)


@manager.command
def test():
    pass


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
