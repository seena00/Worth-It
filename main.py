import places, priceComp, distance, prices
import random

def formatLocations(addresses):
    distances = []
    for i in range(len(addresses)):
        distances.append(distance.calcDist(addresses[i]))
    return distances
def cheapest(locations):
    cheapestPlace = locations[0]
    cheapestPlace2 = locations[0]
    cheapestPlace3 = locations[0]
    for i in range(len(locations)):
        if locations[i].totCost() < cheapestPlace.totCost():
            cheapestPlace = locations[i]
        if locations[i].totCostHalf() < cheapestPlace2.totCostHalf():
            cheapestPlace2 = locations[i]
        if locations[i].totCostFull() < cheapestPlace3.totCostHalf():
            cheapestPlace3 = locations[i]

    sorted = {"gallon":cheapestPlace, "half":cheapestPlace2, "full":cheapestPlace3}
    return sorted

def init():
    #Creating a dictionary with all the names, distances, and addresses
    tempLocations = places.locateGas()
    addresses = tempLocations["addresses"]
    distances = formatLocations(addresses)
    tempLocations = {'names':tempLocations['names'], 'distances':distances, "addresses":addresses, "numbers":tempLocations["numbers"]}
    locations = []

    userCar = priceComp.car(raw_input("Car Name: "), input("Mileage: "))

    #Turning the locations into objects and putting them in a list
    for i in range(len(tempLocations['names'])): #set up location objects
        cost = round(random.uniform(2.1, 3.4), 2) #temporary random number until we get the prices fixed
        name = str(tempLocations["names"][i])
        num = str(tempLocations["numbers"][i])
        print name
        print prices.getPrice(name, num)
        locations.append(priceComp.location(tempLocations["names"][i], prices.getPrice(name, num),
                                            tempLocations["distances"][i], tempLocations["addresses"][i], userCar))


    #displaying the cheapest locations
    sorted = cheapest(locations)
    print "For 1 gallon, {} ({}) is cheapest @ ${:,.2f}".format(sorted["gallon"].name, sorted["gallon"].address, sorted["gallon"].totCost())
    print "For half a tank, {} ({}) is cheapest @ ${:,.2f}".format(sorted["half"].name, sorted["half"].address, sorted["half"].totCostHalf())
    print "For a full tank, {} ({}) is cheapest @ ${:,.2f}".format(sorted["full"].name, sorted["full"].address, sorted["full"].totCostFull())

if __name__ == "__main__":
    init()