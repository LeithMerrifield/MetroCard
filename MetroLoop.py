from Location import Location


class MetroLoop:
    price = 0.10

    def __init__(self, name: str, locations: list) -> None:
        self.locations = locations
        self.name = name

    def __getDistance(self, x: str, y: str) -> int:
        locationA = Location
        locationB = Location

        for stop in self.locations:
            if stop.name == x:
                locationA = stop
        for stop in self.locations:
            if stop.name == y:
                locationB = stop

        return locationB.start - locationA.start

    def getDistance(self, x, y) -> int:
        if type(x) is Location:
            return abs(y.start - x.start)
        else:
            return self.__getDistance(x, y)

    def getTripPrice(self, station1: int, station2: int):
        cost = self.getDistance("Stop {}".format(station1), "Stop {}".format(station2))
        cost *= self.price
        return cost

    def __repr__(self) -> str:
        return "{} {}".format(self.name, self.locations)
