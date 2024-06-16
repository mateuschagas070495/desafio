import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_address_valid(client):
    response = client.get('/get_address?cep=01001000')
    assert response.status_code == 200
    data = response.get_json()
    assert 'logradouro' in data

def test_get_address_invalid(client):
    response = client.get('/get_address?cep=00000000')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'CEP inválido'

def test_get_address_no_cep(client):
    response = client.get('/get_address')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'CEP é obrigatório'
