from geographiclib.geodesic import Geodesic
import csv

class Airport:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

def read_airports_from_csv(filename):
    airports = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            airport = Airport(row['Name'], float(row['Latitude']), float(row['Longitude']))
            airports.append(airport)
    return airports

def find_nearest_location(current_position, locations):
    nearest_location = None
    min_distance = float('inf')
    for location in locations:
        distance = Geodesic.WGS84.Inverse(location.latitude, location.longitude, current_position[0], current_position[1])['s12']
        if distance < min_distance:
            nearest_location = location
            min_distance = distance
    return nearest_location

def check_for_damage():
    # Simulate checking for damage
    return True  # For demonstration purposes, always assume there is damage

def main():
    # Read airports from CSV
    airports = read_airports_from_csv(r'D:\airbnb\airbus\airbus\python\airports.csv')
    
    # Define the flight path
    flight_path = [(40.7128, -74.006), (40.84967033430713, -78.67586478629836), (40.128443476304135, -92.61605962755559), (39.52029944740094, -97.15591464581742), (36.68653433340621, -110.17655028608988), (35.436893089900316, -114.27577549039238), (34.0522, -118.24370000000002)]
    
    # Define current position of the aircraft (last point of the flight path)
    current_position = flight_path[-1]
    
    # Check for damage
    if check_for_damage():
        print("WARNING: Aircraft damage detected. Finding emergency landing sites.")
        nearest_location = find_nearest_location(current_position, airports)
        if nearest_location:
            print("Emergency landing site identified:", nearest_location.name)
        else:
            print("No suitable emergency landing site found nearby.")

if __name__ == "__main__":
    main()
