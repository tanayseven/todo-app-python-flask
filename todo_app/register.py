from todo_app.user.views import blueprint as user_blueprints
from todo_app.extensions import app


def register_all_routes():
    app.register_blueprint(user_blueprints)
