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
    return True  

def main():
    airports = read_airports_from_csv(r'airports.csv')
    flight_path = [(28.7041, 77.1025), (27.132314287571266, 77.15702726774737), (25.560156042875626, 77.21005011058861), (23.98764145899228, 77.26170622038038), (22.414787614009086, 77.31212230772924), (20.84161244388716, 77.36141546004839), (19.268134709773772, 77.4096943292847), (17.694373960271857, 77.45706017608856), (16.12035048912653, 77.50360779277759), (14.546085288752739, 77.54942632386327), (12.971599999999999, 77.5946)]
    current_position = flight_path[-1]
    if check_for_damage():
        print("WARNING: Aircraft damage detected. Finding emergency landing sites.")
        nearest_location = find_nearest_location(current_position, airports)
        if nearest_location:
            print("Emergency landing site identified:", nearest_location.name)
        else:
            print("No suitable emergency landing site found nearby.")

if __name__ == "__main__":
    main()
