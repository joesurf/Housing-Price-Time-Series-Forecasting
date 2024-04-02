import requests
import os

from dotenv import load_dotenv


def get_geocoordinates_from_address(address):
    url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={address}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    
    response = requests.get(url)    
    data = response.json()

    # Check if there are results
    if data['results']:
        first_result = data['results'][0]
        latitude = first_result['LATITUDE']
        longitude = first_result['LONGITUDE']
        print(f"Address: {address}\nCoordinates: Latitude {latitude}, Longitude {longitude}")
    else:
        print("Address not found.")


if __name__ == "__main__":
    get_geocoordinates_from_address("Ang Mo Kio MRT Station")