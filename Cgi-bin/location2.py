#!/usr/bin/env python3
import cgi
from geopy.geocoders import Nominatim
print("Content-type: text/html")
print()

def get_location_info(latitude, longitude):
    geolocator = Nominatim(user_agent="location_app")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    return location.address if location else None

def main():
    # CGI header

    form = cgi.FieldStorage()  # Parse the form data

    latitude = form.getvalue("latitude")
    longitude = form.getvalue("longitude")

    if latitude is not None and longitude is not None:
        try:
            latitude = float(latitude)
            longitude = float(longitude)

            location_info = get_location_info(latitude, longitude)
            if location_info:
                print(f"Location: {location_info}")
            else:
                print("Location not found.")
        except ValueError:
            print("Invalid coordinates.")
    else:
        print("Please provide latitude and longitude.")

if __name__ == "__main__":
    main()
