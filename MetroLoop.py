from Location import Location


class MetroLoop:
    price = 0.10

    def __init__(self, name: str, locations: list) -> None:
        self.locations = locations
        self.name = name

    def getDistance(self, x: str, y: str) -> int:
        locationA = Location
        locationB = Location

        for stop in self.locations:
            if stop.name == x:
                locationA = stop
        for stop in self.locations:
            if stop.name == y:
                locationB = stop

        return locationB.start - locationA.start

    def getDistance(self, x: Location, y: Location) -> int:
        return abs(y.start - x.start)

    def __repr__(self) -> str:
        return "{} {}".format(self.name, self.locations)
