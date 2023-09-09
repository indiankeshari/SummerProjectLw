#!/usr/bin/env python3
import cgi
from geopy.geocoders import Nominatim
print("Content-type: text/html")
def get_real_time_location():
    geolocator = Nominatim(user_agent="real_time_location_app")
    try:
        location = geolocator.geocode("Taj Mahal")
        return location
    except Exception as e:
        return None

def main():
    print("Content-Type: text/html\n")  # CGI header

    form = cgi.FieldStorage()  # Parse the form data

    if "get_location" in form:
        location = get_real_time_location()

        if location:
            print(f"Real-time Location: {location.latitude}, {location.longitude}")
            print(f"Address: {location.address}")
        else:
            print("Location not found. Check your internet connection.")
    else:
        print("Please submit the form to get real-time location.")

if __name__ == "__main__":
    main()