import requests

from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin


class BitcoinApiService(JObtiensLeCoursDuBitcoin):
    def recupere_le_cours_actuel_du_bitcoin(self) -> float:
        response = requests.get('https://api.blockchain.info/stats')
        market_price_usd = response.json()['market_price_usd']
        return market_price_usd
