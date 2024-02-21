import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_list_prizes_with_valid_catalog_id(client):
    response = client.get('/api/catalogs/1/prizes')
    data = response.get_json()

    assert response.status_code == 200
    assert 'total' in data
    assert 'prizes' in data
    assert len(data['prizes']) == 20


def test_list_prizes_with_invalid_catalog_id_1(client):
    response = client.get('/api/catalogs/9999/prizes')
    assert response.status_code == 400


def test_list_prizes_with_invalid_catalog_id_2(client):
    response = client.get('/api/catalogs/prova/prizes')
    assert response.status_code == 400


def test_list_prizes_specific_record(client):
    response = client.get('/api/catalogs/1/prizes?filter[id]=LKHCWNFAIM&pagination[page]=1&pagination[per_page]=8')
    data = response.get_json()
    solution = {
            "prizes": [
                {
                    "description": "Guanti da corsa, colore: rosso",
                    "id": "LKHCWNFAIM",
                    "image": "https://example.com/image1.png",
                    "title": "Prize 1"
                }
            ],
            "total": 1
        }

    assert response.status_code == 200
    assert data == solution


def test_list_prizes_with_invalid_filter(client):
    response = client.get('/api/catalogs/1/prizes?filter[id]=INVALID_ID')
    data = response.get_json()

    assert response.status_code == 200
    assert data['total'] == 0
    assert len(data['prizes']) == 0


def test_list_prizes_with_invalid_page_1(client):
    response = client.get('/api/catalogs/1/prizes?pagination[page]=stringa')
    data = response.get_json()
    assert response.status_code == 400


def test_list_prizes_with_invalid_page_2(client):
    response = client.get('/api/catalogs/1/prizes?pagination[page]=0')
    data = response.get_json()
    assert response.status_code == 400

