import requests
from pytest import mark


@mark.end_to_end
class TestE2E:
    def test_end_to_end_broker(self):
        response = requests.get('http://localhost:5000/broker')

        assert response.status_code == 200
        assert 'can_I_buy_bitcoins' in response.json()

    def test_end_to_end_broker_call_count(self):
        response_before = requests.get('http://localhost:5000/broker_call_count')
        requests.get('http://localhost:5000/broker')
        response_after = requests.get('http://localhost:5000/broker_call_count')

        assert response_after.status_code == 200
        assert response_after.headers["Content-Type"] == "application/json"
        assert response_after.json() - response_before.json() == 1
