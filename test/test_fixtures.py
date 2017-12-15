import pytest
from flask_webtest import TestApp as ApiTestApp

from todo_app.register import register_all_routes
from todo_app.extensions import db, app


class DatabaseFixtures:
    @pytest.fixture(autouse=True)
    def setup(self):
        db.drop_all()
        db.create_all()


class ApiFixtures:
    @pytest.fixture(autouse=True)
    def setup(self):
        register_all_routes()

    @pytest.fixture
    def testapp(self):
        return ApiTestApp(app)
