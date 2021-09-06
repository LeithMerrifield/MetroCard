from Location import Location


class MetroCard:
    funds = 0
    Active = False
    currentStation = Location

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return self.funds
    
    def addFunds(self,amount):
        self.funds += amount
        
    def getFunds(self):
        return self.funds