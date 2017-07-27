from abc import ABC, abstractmethod


class JObtiensLeCoursDuBitcoin(ABC):
    @abstractmethod
    def recupere_le_cours_actuel_du_bitcoin(self) -> float:
        pass
