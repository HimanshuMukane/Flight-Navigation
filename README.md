
# Enhancing Flight Navigation Mechanism for Optimal Route Planning and Risk Mitigation

The project leverages data from various sources, including weather APIs and aviation databases, to identify optimal flight paths while considering challenges such as adverse weather conditions and electronic system failures. The solution provides real-time risk assessment and suggests alternative routes, enhancing safety and efficiency in flight navigation.

## API Reference
Aviation Stack API: https://aviationstack.com
FlightAware API: https://www.flightaware.com/commercial/aeroapi
AviationWeather.gov API: https://www.aviationweather.gov/dataserver
NOAA National Weather Service API: https://www.weather.gov/documentation/services-web-api
OpenWeatherMap API: https://openweathermap.org/api
NASA EOSDIS API: https://earthdata.nasa.gov/eosdis/daacs
FAA NOTAMs API: https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dafd/
ADS-B Exchange API: https://www.adsbexchange.com/data/


#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `https://www.flightaware.com/commercial/aeroapi` | `API` | **FlightAware's AeroAPI is a RESTful API that provides access to FlightAware's flight data. It can be used to get information about flights, including their status, position, and track. The AeroAPI is available in multiple programming languages, including Python.** |
| `https://openweathermap.org/api` | `API` | **PyOWM (Python OpenWeatherMap) is a Python wrapper for the OpenWeatherMap API that allows developers to easily access a wide range of weather data for various locations** |
| `https://docs.mapbox.com/api/overview/` | `API` | **The Mapbox Python SDK is a low-level client API, not a Resource API such as the ones in boto3 or github3.py. Its methods return objects containing HTTP responses from the Mapbox API.** |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Weather Data`| `Real-time Data` | **Includes information on wind speed and direction, temperature, humidity, precipitation, turbulence, and other atmospheric conditions. This data helps in avoiding severe weather and optimizing routes for favorable conditions.** |
| `Air Traffic Data`| `Real-time Data` | **Provides current information on air traffic congestion and the positions of other aircraft to avoid potential collisions and delays.** |
| `Terrain Data`| `Geospatial Data` | **Contains information on the geography and topography of the flight path to avoid obstacles like mountains and ensure safe flight altitudes.** |
| `Aircraft Performance Data`| `Historical and Real-time Data` | **Includes data on fuel consumption, engine performance, and other operational parameters of the aircraft to optimize efficiency and safety.** |
| `Navigation Data`| ` Static and Dynamic Data` | **Encompasses waypoints, airways, and navigational aids that assist in precise route planning and adherence to flight paths.** |
| `Satellite Navigation Data`| `Real-time Data` | **GPS and other satellite data for precise positioning and navigation.** |
| `Risk Assessment Data`| `Analytical Data` | **Evaluates potential risks along the flight path, including security threats, environmental hazards, and technical failures, to plan mitigations.** |
| `Maintenance Data`| `Historical Data` | **Records of aircraft maintenance history to predict and prevent potential technical issues.**|
| `MFuel Data`| `Real-time and Historical Data` | **Information on fuel levels, consumption rates, and availability to ensure sufficient fuel for the planned route.**|

#### add(num1, num2)

Takes two numbers and returns the sum.
def add(num1, num2):
    return num1 + num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add(num1, num2)
print("The sum is:", result)



## Authors

- [@HimanshuMukane](https://github.com/HimanshuMukane)
- [@AdityaBhandare](https://github.com/AdiEmirates)
- [@VivekDhara](https://github.com/DharaVivek)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Demo

Insert gif or link to demo



## Documentation

[Documentation](https://docs.google.com/document/d/10xdtFOiNU6jjQJOj4qxNXW5DZd-FB6LNp4Z3t53sdBE/edit?usp=sharing)


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform
- Data Collection and Management
- Scenario Identification
- Route Planning Algorithm
- User Interface and Dashboard


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd https://github.com/HimanshuMukane/Flight-Navigation
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Tech Stack

**Client:** React, Python, CSS, Javascript

**Server:** Apache, Nginx


## Support

For support, email himanshupm18@gmail.com or join our Slack channel.

