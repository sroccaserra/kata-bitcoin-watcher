from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin


class BitcoinApiFakeService(JObtiensLeCoursDuBitcoin):
    def __init__(self, return_value: float):
        self.return_value = return_value

    def recupere_le_cours_actuel_du_bitcoin(self) -> float:
        return self.return_value
