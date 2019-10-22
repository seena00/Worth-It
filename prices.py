import requests
import urllib
from bs4 import BeautifulSoup

def getPrice(name, number):
    #address = address.split()[0]
    location = urllib.quote_plus(name + " gas")
    url = 'https://google.com/search?q=' + location
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    results = []
    for g in soup.find_all(class_='g'):
        results.append(g.text)
        
    for i in range(len(results)):
        temp = results[i].split()
        for j in range(len(temp)):         
            check = number.split()[1] in temp[j]            
            for g in range(j, len(temp)):
                if check and "/Regular" in temp[g]:
                    return float(str(temp[g]).replace("$", "").replace("/Regular", ""))

    for i in range(len(results)):
        temp = results[i].split()
        for j in temp:
            if "/Regular" in j:
                return float(str(j).replace("$", "").replace("/Regular", ""))
    return 100000
if __name__ == "__main__":
    print getPrice("sam's club", "(816) 942-9048")
