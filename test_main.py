from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# to run this test you need to use 'pytest' commant in terminal
def test_get_all_blog():
    response = client.get('/blog/all')
    assert response.status_code == 200

def test_auth_error():
    response = client.post('/token',
    data={'username': '', 'password': ''}
    )

    access_token = response.json().get('access_token')
    assert access_token == None
    message = response.json().get('detail')[0].get('msg')
    assert message == 'field required'

def test_auth_success():
    response = client.post('/token',
    data={'username': 'lilibet', 'password': 'lilibet'}
    )

    access_token = response.json().get('access_token')
    assert access_token

def test_post_article():
    auth = client.post('/token',
    data={'username': 'lilibet', 'password': 'lilibet'}
    )

    access_token = auth.json().get('access_token')

    assert access_token

    response = client.post(
        '/article/',
        json={
            'title': 'Title',
            'content': 'Content',
            'published': True,
            'creator_id': 2
        },
        headers= {
            'Authorization': 'bearer ' + access_token
        }
    )

    assert response.status_code == 200
    assert response.json().get('title') == 'Title'