class ParkingSpace:
    def __init__(self, space_id: str, location: str):
        self._spaceId = space_id
        self._location = location
    
    def getRawData(self) -> str:
        return f"Space ID: {self._spaceId}, Location: {self._location}"
    
    def getFormat(self) -> str:
        return "json"  