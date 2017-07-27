import requests
from pytest import mark


@mark.end_to_end
class TestE2E:
    def test_end_to_end(self):
        response = requests.get('http://localhost:5000/')

        assert response.text == 'Can I buy bitcoins ? NO'
