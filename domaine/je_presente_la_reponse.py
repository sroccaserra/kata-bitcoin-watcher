from abc import ABC, abstractmethod
from typing import Dict, Any


class JePresenteLaReponse(ABC):
    @abstractmethod
    def est_ce_que_je_peux_acheter(self) -> Dict[str, Any]:
        pass
