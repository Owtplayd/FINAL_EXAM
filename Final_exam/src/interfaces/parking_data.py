from abc import ABC, abstractmethod
from typing import Dict

class IParkingData(ABC):
    @abstractmethod
    def getUsageTime(self) -> int:
        pass
    
    @abstractmethod
    def getSpaceDetails(self) -> Dict:
        pass