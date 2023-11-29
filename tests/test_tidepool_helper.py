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
    expected_times = 'None, None, 7:55 AM, 9:09 AM, 0:02 PM, 0:51 PM, 2:21 PM, 1:37 PM, 1:06 PM, 1:46 PM, 2:23 PM, ' \
                     '2:59 PM, 3:37 PM, 4:16 PM, None, None, None, None, 7:35 AM, 8:56 AM, 0:02 PM, 0:57 PM, 2:35 PM, ' \
                     '1:52 PM, 1:31 PM, 2:20 PM, 3:05 PM, 3:47 PM, 4:26 PM, None'
    expected_heights = '---, ---, 3.51 ft, 3.37 ft, 0.79 ft, 1.16 ft, 2.02 ft, 1.53 ft, 1.4 ft, 0.77 ft, 0.16 ft, ' \
                       '-0.39 ft, -0.85 ft, -1.19 ft, ---, ---, ---, ---, 3.17 ft, 2.84 ft, 0.57 ft, 1.19 ft, 0.77 ft,' \
                       ' 1.78 ft, 0.05 ft, -0.53 ft, -0.9 ft, -1.09 ft, -1.11 ft, ---'
    with requests_mock.Mocker() as m:
        m.get('https://www.tide-forecast.com/locations/TestLocation/tides/latest', text=mock_page)
        tides = Tides("TestLocation")
        get_tide_info(tides)
        assert tides.do_low_times() == expected_times
        assert tides.do_low_heights() == expected_heights


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'text/html' in response.content_type


def test_location_info_page_post(client):
    response = client.post('/location', data=dict(location="TestLocation"))
    assert response.status_code == 200
    # Additional checks can be done on the response data
