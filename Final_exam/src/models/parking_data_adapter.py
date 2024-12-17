from typing import Dict
from ..interfaces.parking_data import IParkingData
from .parking_space import ParkingSpace

class ParkingDataAdapter(IParkingData):
    def __init__(self, source_data: Dict, format: str, parking_space: ParkingSpace):
        self._sourceData = source_data
        self._format = format
        self._parkingSpace = parking_space
    
    def convertData(self) -> 'ParkingDataAdapter':
        # Convert the source data into the required format
        return self
    
    def parseRawData(self, data: str) -> Dict:
        # Parse the raw data string into a dictionary
        # This is a simple implementation - you might want to add more complex parsing
        return eval(data)
    
    def getUsageTime(self) -> int:
        return self._sourceData.get('usage_time', 0)
    
    def getSpaceDetails(self) -> Dict:
        return {
            'space_id': self._parkingSpace._spaceId,
            'location': self._parkingSpace._location,
            'format': self._format
        }