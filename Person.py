from MetroCard import MetroCard


class Person:
    def __init__(self, name) -> None:
        self.card = MetroCard()
        self.name = name
        self.tripHistory = []

    def addFunds(self, amount):
        self.card.addFunds(amount)

    def getFunds(self):
        return "Current Funds: ${}".format(self.card.getFunds())

    def printHistory(self):
        for trip in self.tripHistory:
            print("{} -> {}".format(trip[0], trip[1]))
