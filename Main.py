from Location import Location
from MetroLoop import MetroLoop
from Person import Person

import os

locationList = []

for i in range(1, 13):
    newStop = Location("Stop {}".format(i), i - 1, 12 - i)
    locationList.append(newStop)

mainLoop = MetroLoop("The Frankston Line", locationList)

user1 = Person("Leith")
user1.addFunds(20)

while True:
    print("What is your name: ", end="")
    name = input()
    while True:
        os.system("cls")
        print("Choose an option \n1.Check Balance \n2.Add Funds\n3.Tap On \n4.Cancel")
        try:
            choice = int(input())
        except ValueError:
            print("That was not a valid option")
            continue

        if choice == 1:
            print(user1.getFunds())
        elif choice == 2:
            try:
                funds = int(input("Enter the amount you'd like to add: "))
            except ValueError:
                print("That was not a valid entry")
                continue

            user1.addFunds(funds)
            continue
        elif choice == 3:
            pass
        elif choice == 4:
            break

        if name == user1.name and choice == 3:
            print("What station are you tapping on at? ", end="")
            station1 = input()
            user1.card.Active = True
            # train anim
            print("What station are you tapping off at? ", end="")
            station2 = input()

            cost = mainLoop.getTripPrice(station1, station2)
            print("Your journey cost {} dollars.".format(cost))
            user1.card.addFunds(-cost)

        input("\nPress Any Button Too Continue")
