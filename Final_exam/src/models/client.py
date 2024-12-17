from typing import List, Optional
from ..interfaces.parking_data import IParkingData

class Client:
    def __init__(self, client_id: str, name: str):
        self._clientId = client_id
        self._name = name
        self._usageData: List[IParkingData] = []
    
    def getBill(self) -> float:
        # This will be calculated by the billing system
        pass
    
    def getUsageData(self) -> List[IParkingData]:
        return self._usageData
    
    def add_usage_data(self, data: IParkingData):
        self._usageData.append(data)
