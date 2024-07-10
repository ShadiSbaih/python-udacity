import requests

API_ROOT = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = 'd97d322d59a9f14637cbfe397da169ac'  # Your actual OpenWeatherMap API key

def fetch_location(query):
    # OpenWeatherMap doesn't need a separate location fetch, using query directly
    return {'name': query}

def fetch_weather(location):
    params = {
        'q': location['name'],
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_ROOT, params=params)
    return response.json()

def disambiguate_locations(locations):
    # OpenWeatherMap does not require this function, as it directly fetches weather by city name
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['name']}")

def display_weather(weather):
    if weather['cod'] != 200:
        print("\nError fetching weather data:", weather['message'])
        return
    name = weather['name']
    main = weather['weather'][0]['main']
    description = weather['weather'][0]['description']
    temp = weather['main']['temp']
    temp_min = weather['main']['temp_min']
    temp_max = weather['main']['temp_max']

    print(f"Weather for {name}:")
    print(f"Condition: {main} - {description}")
    print(f"Temperature: {temp:.1f}°C")
    print(f"High: {temp_max:.1f}°C")
    print(f"Low: {temp_min:.1f}°C")

def weather_dialog():
    try:
        where = ''
        while not where:
            where = input("Where in the world are you?\n ")
        location = fetch_location(where)
        weather = fetch_weather(location)
        display_weather(weather)
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Is the network up?\n")

if __name__ == '__main__':
    while True:
        weather_dialog()
