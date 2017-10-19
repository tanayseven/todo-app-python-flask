import pytest
from webtest.app import TestApp as AppClient

from todo_app.extensions import db, app


class DatabaseFixtures:
    @pytest.fixture(autouse=True)
    def setup(self):
        db.drop_all()
        db.create_all()


class ApiFixtures:
    @pytest.fixture
    def testapp(self):
        return AppClient(app)
