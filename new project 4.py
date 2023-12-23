import requests
import json

# Replace with your OpenWeatherMap API key
api_key = "9377fc27d91ed31e5f377b2ad1c25e4c"

def get_weather(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for error status codes

        inputt = json.loads(response.text)

        # Extract relevant information
        city = inputt['name']
        temperature = inputt['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        humidity = inputt['main']['humidity']
        weather = inputt['weather'][0]['description']

        return city, temperature, humidity, weather

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None, None, None, None

def main():
    while True:
        location = input("Enter a city or ZIP code: ")

        # Validate input (optional)
        if not location:
            print("Please enter a valid location.")
            continue

        city, temperature, humidity, weather = get_weather(location)

        if city:
            print("Weather for", city)
            print("Temperature:", temperature, "Celsius")
            print("Humidity:", humidity, "%")
            print("Weather:", weather)
            break
        else:
            print("Weather data not found for that location.")

if __name__ == "__main__":
    main()
