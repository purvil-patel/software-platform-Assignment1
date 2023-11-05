import pytest
from app import app, get_db_connection, get_post

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# test the database connection
def test_get_db_connection():
    conn = get_db_connection()
    assert conn is None
    conn.close()

#test the index function
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
        
#test the create function
def test_create_post(client):
    new_post = {
        'title': 'Test Post',
        'content': 'This is a test post.'
    }
    response = client.post('/create', data=new_post, follow_redirects=True)
    assert response.status_code == 200
    

