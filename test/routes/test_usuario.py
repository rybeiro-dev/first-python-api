from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_index():
    response = client.get("/usuarios")
    data = [{'id': 1, 'nome': 'Fabio', 'email': 'fabio@fabio.com'}]
    assert response.status_code == 200
    assert response.json() == data


