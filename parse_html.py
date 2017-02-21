from bs4 import BeautifulSoup
#parse html document tree

def options(soup,id):
    option_values = []
    carrier_list = soup.find(id = id) #find the fisrt descendant element in this docuemnt tree where
    for option in carrier_list.find_all('option'): #find descendants that are option tags/elements
        option_values.append(option['values']) #pull out 'value' attribute's value
    return option_values

def print_list(label,codes):
    print("\n%s" % label)
    for c in codes:
        print(c)

def main():
    soup = BeautifulSoup(open('virgin_and_airport.html')) #pass back top-level elements for this HTML
    codes = options(soup,'CarrierList')
    print_list('Carriers',codes)

    codes = options(soup,'AirportList')
    print_list('Airports',codes)

#quiz
def extract_data(page):
    data = {"eventvalidation": "", #these values are used to validate the request
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml")
        ev = soup.find(id="__EVENTVALIDATION") #i'm super doubt the deifnition of top-level...
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

    return data
