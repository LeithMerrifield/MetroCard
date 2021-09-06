from Location import Location
from MetroLoop import MetroLoop
from Person import Person

locationList = []

for i in range(1, 13):
    newStop = Location("Stop {}".format(i), i - 1, 12 - i)
    locationList.append(newStop)

MainLoop = MetroLoop("The Frankston Line", locationList)

user1 = Person("Leith")
user1.addFunds(20)
print(user1.getFunds())
