from abc import ABC, abstractmethod


class JAutoriseAAcheter(ABC):
    @abstractmethod
    def est_ce_que_je_peux_acheter(self) -> bool:
        pass
