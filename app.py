import requests
from flask import Flask

app = Flask(__name__)


# tester est_ce_que_je_peux_acheter("une phrase")


@app.route("/")
def hello():
    try:
        market_price_usd = recupere_le_cours_actuel_du_bitcoin()
    except Exception:
        return "Can I buy bitcoins ? NO"
    else:
        can_i_buy = est_ce_que_je_peux_acheter(market_price_usd)

        return "Can I buy bitcoins ? " + ("YES" if can_i_buy else "NO")


def recupere_le_cours_actuel_du_bitcoin():
    response = requests.get('https://api.blockchain.info/stats')
    market_price_usd = response.json()['market_price_usd']
    return market_price_usd


def est_ce_que_je_peux_acheter(prix):
    return prix < 2401
