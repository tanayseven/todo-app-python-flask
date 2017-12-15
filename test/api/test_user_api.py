from test.test_fixtures import DatabaseFixtures, ApiFixtures


class TestNewUserCreation(DatabaseFixtures, ApiFixtures):
    def test_new_user_creation_should_succeed(self, testapp):
        res = testapp.post_json('/user/register', {
            "user_name": "tanay.p",
            "password": "1234",
            "email": "tanay.p@1234.com",
            "first_name": "Tanay",
            "last_name": "PrabhuDesai"
        })
        assert res.status_code == 200

    def test_all_api_should_return_list_of_all_users(self, testapp):
        res = testapp.get('/user/all')
        assert res.status_code == 200
