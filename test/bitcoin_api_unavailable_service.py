from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin


class BitcoinApiUnavailableService(JObtiensLeCoursDuBitcoin):
    def recupere_le_cours_actuel_du_bitcoin(self) -> float:
        raise Exception()
