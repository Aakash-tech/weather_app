import requests

# Add your own OpenWeatherMap API key
API_KEY = "API_KEY"  

def fetch_weather(city):
    """Fetch weather data for a given city."""
    # Construct the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    # Sending request
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    else:
        return None

def print_weather_report(city, weather_data):
    """Print the weather report for a given city."""
    print("\nWeather Report for:", city)
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Description:", weather_data["weather"][0]["description"])
    print("Humidity:", weather_data["main"]["humidity"], "%")

if __name__ == "__main__":
    # Ask the user for a city name
    city = input("Enter a city name: ")

    # Fetch weather data
    weather_data = fetch_weather(city)

    if weather_data:
        # Print the weather report
        print_weather_report(city, weather_data)
    else:
        print("Error: city not found.")
