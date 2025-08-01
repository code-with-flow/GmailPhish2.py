import time
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Print logo
def print_logo():
    print("""
\033[1;32m
██╗   ██╗ ██████╗ ██╗██████╗ 
██║   ██║██╔═══██╗██║██╔══██╗
██║   ██║██║   ██║██║██████╔╝
╚██╗ ██╔╝██║   ██║██║██╔═══╝ 
 ╚████╔╝ ╚██████╔╝██║██║     
  ╚═══╝   ╚═════╝ ╚═╝╚═╝     
\033[0m
""")

# Phone number lookup class
class PhoneTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.geocoder = OpenCageGeocode(api_key)

    def parse_phone_number(self, number):
        try:
            return phonenumbers.parse(number)
        except phonenumbers.NumberParseException:
            return None

    def get_timezone(self, phone_number):
        try:
            time_zones = timezone.time_zones_for_number(phone_number)
            return time_zones
        except Exception as e:
            return f"Error retrieving timezone: {str(e)}"

    def get_location(self, phone_number):
        try:
            location = geocoder.description_for_number(phone_number, "en")
            return location
        except Exception as e:
            return f"Error retrieving location: {str(e)}"

    def get_carrier(self, phone_number):
        try:
            carrier_name = carrier.name_for_number(phone_number, "en")
            return carrier_name
        except Exception as e:
            return f"Error retrieving carrier: {str(e)}"

    def get_map(self, location):
        try:
            query = str(location)
            results = self.geocoder.geocode(query)
            if not results:
                return "No location data found."
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            my_map = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(my_map)
            my_map.save("Location.html")
            return "Map saved as Location.html"
        except Exception as e:
            return f"Error generating map: {str(e)}"

    def check_phonenumber(self):
        while True:
            print("""
1. Lookup phonenumber
2. Track phonenumber location
3. Check Service carrier (SIM card)
4. Exit
""")
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                number = input("Enter the PhoneNumber with the country code (e.g., +918897909596): ")
                phone_number = self.parse_phone_number(number)
                if not phone_number:
                    print("Invalid phone number format.")
                    continue
                time_zones = self.get_timezone(phone_number)
                print(f"Target's current timezone: {time_zones}")
            elif choice == "2":
                number = input("Enter the PhoneNumber with the country code (e.g., +918897909596): ")
                phone_number = self.parse_phone_number(number)
                if not phone_number:
                    print("Invalid phone number format.")
                    continue
                location = self.get_location(phone_number)
                print(f"Location: {location}")
                if "Error" not in location:
                    map_result = self.get_map(location)
                    print(map_result)
            elif choice == "3":
                number = input("Enter the PhoneNumber with the country code (e.g., +918897909596): ")
                phone_number = self.parse_phone_number(number)
                if not phone_number:
                    print("Invalid phone number format.")
                    continue
                carrier_name = self.get_carrier(phone_number)
                print(f"Service carrier: {carrier_name}")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    print_logo()
    # Replace with your actual OpenCage API key
    api_key = input("Enter your OpenCage API key (get one at https://opencagedata.com/api): ")
    tracker = PhoneTracker(api_key)
    tracker.check_phonenumber()
