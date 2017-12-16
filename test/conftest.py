import pytest

from todo_app.extension import app


@pytest.fixture()
def client():
    app.testing = True
    return app.test_client()
