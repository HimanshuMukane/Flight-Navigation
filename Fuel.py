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
    airports = read_airports_from_csv(r'airports.csv')
    
    # Define the flight path
    flight_path =[(28.7041, 77.1025), (27.132314287571266, 77.15702726774737), (25.560156042875626, 77.21005011058861), (23.98764145899228, 77.26170622038038), (22.414787614009086, 77.31212230772924), (20.84161244388716, 77.36141546004839), (19.268134709773772, 77.4096943292847), (17.694373960271857, 77.45706017608856), (16.12035048912653, 77.50360779277759), (14.546085288752739, 77.54942632386327), (12.971599999999999, 77.5946)]
    
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
