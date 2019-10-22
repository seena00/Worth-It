import urllib
import json

apiKey = "Your API Key" #apiKey for google maps

def coords():
    endpoint = "http://freegeoip.net/json"
    response = urllib.urlopen(endpoint).read()
    results = json.loads(response)
    #return "38.835657, -94.691855"
    return str(results["latitude"]) + ", " + str(results["longitude"])

def locateGas():
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    
    origin = coords()

    nav_request = "location={}&type={}&rankby={}&key={}".format(origin, "gas_station", "distance", apiKey)

    request = endpoint + nav_request
    response = urllib.urlopen(request).read()

    results = json.loads(response)

    tempPlaces = results["results"]
    names = []
    addresses = []
    numbers = []
    for i in range (5): #listing the places
        names.append(tempPlaces[i]["name"])
        addresses.append(tempPlaces[i]["vicinity"])
        numbers.append(getDetails(tempPlaces[i]["place_id"]))
    locations = {"names":names, "addresses":addresses, "numbers": numbers}
    
    return locations

def getDetails(placeID):
    #trying to find the prices
    endpointDetails = "https://maps.googleapis.com/maps/api/place/details/json?"
    
    nav_request = "place_id={}&key={}".format(placeID, apiKey)
    request = endpointDetails + nav_request

    response = urllib.urlopen(request).read()
    results = json.loads(response)["result"]
    return results["formatted_phone_number"]

if __name__ == "__main__":
    locations = locateGas()
    print locations
    #printDetails(locations)
