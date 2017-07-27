import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    response = requests.get('https://api.blockchain.info/stats')
    market_price_usd = response.json()['market_price_usd']
    can_i_buy = market_price_usd < 2596.22
    return "Can I buy bitcoins ? " + ("YES" if can_i_buy else "NO")
