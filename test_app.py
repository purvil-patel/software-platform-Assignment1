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
    assert conn is not None
    conn.close()

#test the index function
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    # Further assertions can be made on the response data
        
#test the create function
def test_create_post(client):
    new_post = {
        'title': 'Test Post',
        'content': 'This is a test post.'
    }
    response = client.post('/create', data=new_post, follow_redirects=True)
    assert response.status_code == 200
    # Further assertions to check if the post was added to the database

# test the edit function
# def test_edit_post(client):
#     edited_post = {
#         'title': 'Edited Test Post',
#         'content': 'This is an edited test post.'
#     }
#     response = client.post('/1/edit', data=edited_post, follow_redirects=True)
#     print("Purvil Print the state ")
#     print(response)
#     assert response.status_code == 200
#     # Further assertions to check if the post was edited in the database

# #test the delete function
# def test_delete_post(client):
#     response = client.post('/1/delete', follow_redirects=True)
#     assert response.status_code == 200
#     # Further assertions to check if the post was deleted from the database

# #test the 404 error
# def test_404(client):
#     response = client.get('/doesnotexist')
#     assert response.status_code == 404
#     assert b'Page not found' in response.data       

# #test the 500 error
# def test_500(client):
#     response = client.get('/500')
#     assert response.status_code == 500
#     assert b'Server error' in response.data

# # test the get_post function
# def test_get_post():        
#     post = get_post(1)
#     assert post is not None 


