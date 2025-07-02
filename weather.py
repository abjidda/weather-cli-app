import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
        return
    print("\nCurrent Weather:")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description'].capitalize()}")

def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(FORECAST_URL, params=params)
    data = response.json()
    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Unable to fetch forecast data')}")
        return
    print("\n5-Day Forecast:")
    for item in data["list"][:5]:  # Show next 5 time slots (~15 hours)
        print(f"Date & Time: {item['dt_txt']}")
        print(f"Temperature: {item['main']['temp']}°C")
        print(f"Weather: {item['weather'][0]['description'].capitalize()}")
        print("-" * 20)

def save_search(city):
    with open("search_history.txt", "a") as file:
        file.write(city + "\n")

def main():
    while True:
        city = input("\nEnter a city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)
        get_forecast(city)
        save_search(city)

if __name__ == "__main__":
    main()
