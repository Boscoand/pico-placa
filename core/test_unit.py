import pytest

from api import app
from datetime import datetime

ENDPOINT = '/api/query'

def get_endpoint(license_plate, date, time):
    return ENDPOINT + '?license_plate=' + license_plate + '&date=' + str(date) + '&time=' + str(time)

@pytest.fixture(scope='module')
def test_client():
    yield app.test_client()

def test_available_weekend(test_client):
    """Verifies if a"""
    
    license_plate = 'MCM4111'
    date = '2020-02-29'
    time = '7:30'

    response = test_client.get(get_endpoint(license_plate, date, time))
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response['available'] == True
    assert json_response['day'] == 'Sábado'

def test_available_datetime(test_client):
    """Verifies if a"""
    
    license_plate = 'MCM4111'
    date = '2020-03-02'
    time = '12:00'

    response = test_client.get(get_endpoint(license_plate, date, time))
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response['available'] == True
    assert json_response['day'] == 'Lunes'

def test_unavailable_datetime(test_client):
    """Verifies if a"""
    
    license_plate = 'MCM4111'
    date = '2020-03-02'
    time = '08:00'

    response = test_client.get(get_endpoint(license_plate, date, time))
    json_response = response.get_json()

    assert response.status_code == 200
    assert json_response['available'] == False
    assert json_response['day'] == 'Lunes'