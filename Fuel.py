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

def find_nearest_port(current_position, ports):
    nearest_port = None
    min_distance = float('inf')
    for port in ports:
        distance = Geodesic.WGS84.Inverse(port.latitude, port.longitude, current_position[0], current_position[1])['s12']
        if distance < min_distance:
            nearest_port = port
            min_distance = distance
    return nearest_port

def main():
    # Read airports from CSV
    airports = read_airports_from_csv(r'D:\airbnb\airbus\airbus\python\airports.csv')
    
    # Define the flight path
    flight_path = [(40.7128, -74.006), (40.84967033430713, -78.67586478629836), (40.128443476304135, -92.61605962755559), (39.52029944740094, -97.15591464581742), (36.68653433340621, -110.17655028608988), (35.436893089900316, -114.27577549039238), (34.0522, -118.24370000000002)]
    
    # Define current position of the aircraft (last point of the flight path)
    current_position = flight_path[-1]
    
    # Determine fuel level (assumed to be provided)
    current_fuel_level = float(input("Enter current fuel level (in liters): "))
    
    # Check fuel level and suggest nearest port if low
    if current_fuel_level < 200:  # Threshold for low fuel level, e.g., 200 liters
        nearest_port = find_nearest_port(current_position, airports)
        if nearest_port:
            print("WARNING: Low fuel level detected. Nearby port for refueling:", nearest_port.name)
        else:
            print("No nearby port found for refueling.")

if __name__ == "__main__":
    main()
