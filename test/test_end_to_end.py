import requests
from pytest import mark


@mark.end_to_end
class TestE2E:
    def test_end_to_end(self):
        response = requests.get('http://localhost:5000/broker')

        assert response.status_code == 200
        assert 'can_I_buy_bitcoins' in response.json()
