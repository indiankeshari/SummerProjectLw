#!/usr/bin/env python3


import cgi
import geocoder
from geopy.geocoders import Nominatim

print("Content-type: text/html")
print()


def get_live_coordinates():
    # Get the location based on the current IP address
    location = geocoder.ip('me')

    # Check if the location was successfully retrieved
    if location.latlng:
        latitude, longitude = location.latlng
        return latitude, longitude
    else:
        return None, None

def get_location_info(latitude, longitude):
    geolocator = Nominatim(user_agent="location_app")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    return location.address if location else None

def main():
    # Get the form data
    form = cgi.FieldStorage()

    # Check if the button with name "get_coordinates" was clicked
    if "get_coordinates" in form:
        latitude, longitude = get_live_coordinates()

        if latitude is not None and longitude is not None:        
            print("Your Latitude and Longitude are:", latitude, longitude)
            location_info = get_location_info(latitude, longitude)
            if location_info:
                print(f"Your Location: {location_info}")
               
            else:
                print("Location information not found.")
               
        else:
            print("Unable to retrieve coordinates.")
        

if __name__ == "__main__":
    main()