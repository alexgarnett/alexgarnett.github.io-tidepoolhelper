from tidepool_helper.tidepool_helper import app, get_tide_info, Tides
import requests_mock
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_tides_initialization():
    tides = Tides("TestLocation")
    assert tides.location == "TestLocation"
    assert tides.low_times == []
    assert tides.low_heights == []


def test_get_tide_info():
    with open('tests/mock_page.txt', 'r') as page:
        mock_page = page.read()
    expected_time = '3:35PM'
    expected_height = '0.17'
    with requests_mock.Mocker() as m:
        m.get('https://www.tide-forecast.com/locations/TestLocation/tides/latest', text=mock_page)
        tides = Tides("TestLocation")
        get_tide_info(tides)
        assert tides.low_times == [expected_time]
        assert tides.low_heights == [expected_height]


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'text/html' in response.content_type


def test_location_info_page_post(client):
    response = client.post('/location', data=dict(location="TestLocation"))
    assert response.status_code == 200
    # Additional checks can be done on the response data
