import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from datetime import datetime
import csv

app = Flask(__name__)
CORS(app)  # Enable CORS for this Flask app
from geographiclib.geodesic import Geodesic
import heapq

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



def find_nearest_port(current_position, ports):
    nearest_port = None
    min_distance = float('inf')
    for port in ports:
        distance = Geodesic.WGS84.Inverse(port.latitude, port.longitude, current_position[0], current_position[1])['s12']
        if distance < min_distance:
            nearest_port = port
            min_distance = distance
    return nearest_port


def check_for_damage():
    return True  

def compute_geodesic_points(start_point, end_point, num_points):
    geod = Geodesic.WGS84
    geodesic_line = geod.InverseLine(start_point[0], start_point[1], end_point[0], end_point[1])
    points = []
    for i in range(num_points + 1):
        interp = geodesic_line.Position(i * geodesic_line.s13 / num_points)
        points.append((interp['lat2'], interp['lon2']))
    return points

def heuristic_distance(point, goal):
    dx = goal[0] - point[0]
    dy = goal[1] - point[1]
    return ((dx ** 2) + (dy ** 2)) ** 0.5

def astar(start, goal, obstacles, num_points):
    geod = Geodesic.WGS84
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
        for next_point in compute_geodesic_points(current, goal, num_points):
            if next_point not in obstacles:
                new_cost = cost_so_far[current] + heuristic_distance(current, next_point)
                if next_point not in cost_so_far or new_cost < cost_so_far[next_point]:
                    cost_so_far[next_point] = new_cost
                    priority = new_cost + heuristic_distance(next_point, goal)
                    heapq.heappush(frontier, (priority, next_point))
                    came_from[next_point] = current
    path = [goal]
    while goal != start:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path

def fetch_real_time_weather_data(api_key, city_name):
    # city_name = "mumbai"
    # print(city_name)
    # print(api_key)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    json_data = response.json()
    if isinstance(json_data, list):
        for item in json_data:
            # print(item)
            pass
    elif isinstance(json_data, dict):
        for key, value in json_data.items():
            # print(f"{key}: {value}")
            pass
        print(" ")
        print(" ")
    else:
        print(json_data, "Hello")
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'precipitation': data['weather'][0]['main'],  
            'temp_max': data['main']['temp_max'] - 273.15, 
            'temp_min': data['main']['temp_min'] - 273.15,  # Convert from Kelvin to Celsius
            'wind': data['wind']['speed']
        }
        # return pd.DataFrame([weather_data])
        return json_data
    else:
        print("Error fetching weather data:", response.status_code)
        return None

@app.route('/your_flask_route', methods=['POST'])
def your_flask_route():
    start_latitude = float(request.json.get('start_latitude'))
    start_longitude = float(request.json.get('start_longitude'))
    city_name = request.json.get('city_name')
    end_latitude = float(request.json.get('end_latitude'))
    end_longitude = float(request.json.get('end_longitude'))
    obstacle_points_latitude1 = float(request.json.get('obstacle_points_latitude1'))
    obstacle_points_longitude1 = float(request.json.get('obstacle_points_longitude1'))
    obstacle_points_latitude2 = float(request.json.get('obstacle_points_latitude2'))
    obstacle_points_longitude2 = float(request.json.get('obstacle_points_longitude2'))
    api_key = "ca8c2c7970a09dc296d9b3cfc4d06940"
    output = fetch_real_time_weather_data(api_key, city_name)

    start_point = (start_latitude, start_longitude) 
    end_point = (end_latitude, end_longitude)  

    obstacle_points = [
        (obstacle_points_latitude1, obstacle_points_longitude1),
        (obstacle_points_latitude2, obstacle_points_longitude2)   
    ]

    num_points = 10
    shortest_path = compute_geodesic_points(start_point, end_point, num_points)
    if any(point in obstacle_points for point in shortest_path):
        print("Obstacles detected in shortest path by GeographicLib.")
        print("Finding alternative path using A* algorithm.")
        for delta_lat in [-1, 0, 1]:
            for delta_lon in [-1, 0, 1]:
                adjusted_start_point = (start_point[0] + delta_lat, start_point[1] + delta_lon)
                adjusted_end_point = (end_point[0] + delta_lat, end_point[1] + delta_lon)
                alternative_path = astar(adjusted_start_point, adjusted_end_point, obstacle_points, num_points)
                if all(point not in obstacle_points for point in alternative_path):
                    print("Alternative path without obstacles:")
                    print(alternative_path)
                    break
            else:
                continue
            break
    else:
        print("Shortest path by GeographicLib (no obstacles):")
    airports = read_airports_from_csv(r'airports.csv')
    current_position = shortest_path[-1]
    current_fuel_level = float(10)
    if current_fuel_level < 20:  
        nearest_port = find_nearest_port(current_position, airports)
        if nearest_port:
            print("WARNING: Low fuel level detected. Nearby port for refueling:", nearest_port.name)
        else:
            nearest_port = None
            print("No nearby port found for refueling.")

    if check_for_damage():
        print("WARNING: Aircraft damage detected. Finding emergency landing sites.")
        nearest_location = find_nearest_location(current_position, airports)
        if nearest_location:
            print("Emergency landing site identified:", nearest_location.name)
        else:
            print("No suitable emergency landing site found nearby.")

    response_data = {"message": tuple(shortest_path), "weather_d": output, "nearest_port": nearest_port.name}
    print(response_data,"my json data")
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=5000)
