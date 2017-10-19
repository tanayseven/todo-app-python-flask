import pytest as pytest

from test.test_fixtures import DatabaseFixtures
from todo_app.extensions import db
from todo_app.user.repos import ListUserRepo


class TestAdminRepo(DatabaseFixtures):
    def test_when_a_user_is_created_we_should_be_able_to_load_it_with_credentials(self):
        ListUserRepo.add_new_user(
            user_name='tanay',
            password='12345',
            email='tanay@1234.com',
            first_name='Tanay',
            last_name='PrabhuDesai',
        )
        user = ListUserRepo.load_user_with_credentials(user_name='tanay', password='12345')
        assert user is not None
