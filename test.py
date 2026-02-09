from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_get_closing_price_app_returns_200():
    """Test that the endpoint returns a 200 status code."""
    response = client.post('/get_closing_price_app')
    assert response.status_code == 200


def test_get_closing_price_app_returns_closing_price():
    """Test that the endpoint returns the expected response."""
    response = client.post('/get_closing_price_app')
    assert response.json() == "Closing price"
