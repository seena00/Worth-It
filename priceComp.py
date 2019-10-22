import random

class car(object):
    name = ""
    mileage = 0.0

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def calcMileage(self, distance): #calculates the gas lost driving to the gas station using the dist and mileage
        return float(distance/self.mileage)

class location(object):
    name = " "
    cost = 0.0
    distance = 0.0
    galsLost = 0.0

    def __init__(self, name, cost, distance, address, userCar):
        self.name = name
        self.cost = cost
        self.distance = distance
        self.address = address
        self.galsLost = userCar.calcMileage(self.distance)

    def totCost(self):
        return round((self.cost*(1+self.galsLost)), 2)
    def totCostHalf(self):
        return round((self.cost*6 + self.galsLost*self.cost), 2)
    def totCostFull(self):
        return round((self.cost*12 + self.galsLost*self.cost), 2)
    def allData(self):
        print "place:", self.name + "; cost:", "${:,.2f}".format((self.cost)) + "; distance:", str(self.distance) \
                            + "; total cost:", "${:,.2f}".format(self.totCost())


if __name__ == "__main__":
    ##running tests:
    Car = car("crv", 32) #test case car for all tests

    ##testing comparison thing
    places = ["Shell", "BP", "QT", "Phillips 66", "Costco"]

    for i in range(len(places)):
        places[i] = location(places[i], round(random.uniform(2.1, 3.4), 2), round(random.randint(3, 20), 2))
        places[i].allData()

    cheapestPlace = places[0]
    cheapestPlace2 = places[0]
    cheapestPlace3 = places[0]
    for i in range(len(places)):
        if  places[i].totCost() < cheapestPlace.totCost():
            cheapestPlace = places[i]
        if places[i].totCostHalf() < cheapestPlace2.totCostHalf():
            cheapestPlace2 = places[i]
        if places[i].totCostFull() < cheapestPlace3.totCostHalf():
            cheapestPlace3 = places[i]

    print "\nThe cheapest place is", cheapestPlace.name, "with a price of", '${:,.2f}'.format(cheapestPlace.totCost())

    print "\nHalf Tank:", cheapestPlace2.name, cheapestPlace2.totCostHalf()
    print "\nFull Tank:", cheapestPlace3.name, cheapestPlace3.totCostFull()