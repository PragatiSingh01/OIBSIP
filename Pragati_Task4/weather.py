import requests

print("===== Weather App =====")

city = input("Enter city name: ")

API_KEY = "63afe424d1f495b4e082bd555b218ee0" 

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        print("\n------ Weather Report ------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Weather:", condition)
        print("Wind Speed:", wind, "m/s")

    else:
        print("Error:", data["message"])

except:
    print("Internet connection issue or invalid API.")