from main import app

def test_get_api_endpoint():
    with app.test_client() as c:
        response = c.get('api/DemoApiEndpoint')
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response == {'message': 'This is a response from a GET request.'}

def test_post_api_endpoint():
    with app.test_client() as c:
        response = c.post('api/DemoApiEndpoint', json={
            "name": "User"
        })
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response == {'message': 'Nice to meet you, User!'}

# test_api_endpoint()
# test_post_api_endpoint()
