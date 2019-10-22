import urllib
import json

def coords():
    endpoint = "http://freegeoip.net/json"
    response = urllib.urlopen(endpoint).read()
    results = json.loads(response)

    #return "38.835657, -94.691855"
    return str(results["latitude"]) + ", " + str(results["longitude"])
	
def calcDist(destination):
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    apiKey = "YOUR API KEY"

    origin = coords()
    destination = destination.replace(" ", "+")

    nav_request = "origin={}&destination={}&key = {}".format(origin, destination, apiKey)

    request = endpoint + nav_request
    response = urllib.urlopen(request).read()

    directions = json.loads(response)


    distance = directions["routes"][0]["legs"][0]["distance"]["text"]

    return float(distance.replace("mi", ""))

if __name__ == "__main__":
    destination = raw_input("Where do you want to go:? ").replace(" ", "+")
    distance = calcDist(destination)
    print "You are", distance, "away from", destination
