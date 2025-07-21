import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "multiplication-service"}

def test_multiplication_success():
    """Test successful multiplication operation."""
    response = client.get("/?first_number=5&second_number=3")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 15.0
    assert data["operation"] == "multiplication"
    assert data["first_number"] == 5.0
    assert data["second_number"] == 3.0

def test_multiplication_with_decimals():
    """Test multiplication with decimal numbers."""
    response = client.get("/?first_number=2.5&second_number=4")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 10.0

def test_multiplication_by_zero():
    """Test multiplication by zero."""
    response = client.get("/?first_number=100&second_number=0")
    assert response.status_code == 200
    assert response.json()["result"] == 0.0

def test_multiplication_negative_numbers():
    """Test multiplication with negative numbers."""
    response = client.get("/?first_number=-5&second_number=3")
    assert response.status_code == 200
    assert response.json()["result"] == -15.0

def test_multiplication_default_values():
    """Test multiplication with default values (0*0)."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["result"] == 0.0

def test_multiplication_negative_by_negative():
    """Test multiplication of two negative numbers."""
    response = client.get("/?first_number=-5&second_number=-3")
    assert response.status_code == 200
    assert response.json()["result"] == 15.0