def test_root(client):
    response = client.get('/')
    print(response.data)
    assert True
