import requests
import responses

# Define a simple function that makes an HTTP request using the requests library
def make_api_request(url):
    response = requests.get(url)
    return response.json()

# Test the function with a mocked server response
@responses.activate
def test_make_api_request():
    # Mock the server response for a specific URL
    responses.add(responses.GET, 'https://api.example.com/data', json={'key': 'value'}, status=200)

    # Call the function with the mocked URL
    result = make_api_request('https://api.example.com/data')

    # Verify that the function returned the expected result based on the mocked response
    assert result == {'key': 'value'}

# Run the test
test_make_api_request()
