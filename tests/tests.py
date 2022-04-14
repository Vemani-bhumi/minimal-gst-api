from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post('/users/', json={"username":"abcdefg","password":"password123","role":"taxpayer"})

    assert response.status_code == 201
    
    
