import requests

def get_weather(city):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=f81876c0088f37930d7c80b6f89bcf68".format(city)

    json_data = requests.get(url).json()

    result = {}
    result["weather"] = json_data["weather"][0]["description"]
    result["temp"] = int(json_data["main"]["temp"] - 273.15)      ## conversion between Fahrenheit and Celsius
    result["feels_like"] = int(json_data["main"]["feels_like"] - 273.15)
    result["temp_min"] = int(json_data["main"]["temp_min"] - 273.15)
    result["temp_max"] = int(json_data["main"]["temp_max"] - 273.15)


    return result

if __name__ == "__main__":
    result = get_weather("Darmstadt")
    print(result)