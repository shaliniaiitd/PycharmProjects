pytest
import pytest
import requests

@pytest.fixture
def api_client():
    # Create an API client session
    session = requests.Session()
    yield session
    # Clean up resources after the test
    session.close()

def test_api(api_client):
    # Make an API request
    response = api_client.get('https://api.example.com/endpoint')

    # Perform assertions on the response
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert 'data' in response.json()
