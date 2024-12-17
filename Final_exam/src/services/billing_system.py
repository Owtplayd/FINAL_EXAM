from typing import List
from ..models.client import Client
from ..interfaces.parking_data import IParkingData

class Invoice:
    def __init__(self, client: Client, amount: float):
        self.client = client
        self.amount = amount
        self.generated_date = None 

class BillingSystem:
    def __init__(self, hourly_rate: float):
        self._hourlyRate = hourly_rate
        self._parkingData: List[IParkingData] = []
    
    def calculateBill(self, client: Client) -> float:
        total_time = 0
        for usage in client.getUsageData():
            total_time += usage.getUsageTime()
        return total_time * self._hourlyRate
    
    def generateInvoice(self, client: Client) -> Invoice:
        amount = self.calculateBill(client)
        return Invoice(client, amount)