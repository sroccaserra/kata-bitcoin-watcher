from abc import ABC, abstractmethod


class JePresenteLaReponse(ABC):
    @abstractmethod
    def est_ce_que_je_peux_acheter(self) -> str:
        pass