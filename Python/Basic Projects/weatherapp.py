import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"  # Get from https://openweathermap.org/api
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

if response["cod"] == 200:
    print(f"City: {response['name']}")
    print(f"Temperature: {response['main']['temp']}°C")
    print(f"Weather: {response['weather'][0]['description']}")
else:
    print("City not found!")
