# modules and global variables
from abc import abstractmethod, ABC
import requests


# abstract class
class WeatherAbstract(ABC):

    @abstractmethod
    def get_current_weather(self, lat, lon):
        pass


# openweather class
class OpenWeatherProvider(WeatherAbstract):

    base_url = "https://api.openweathermap.org/data/3.0/onecall"

    def init(self, api_key):
        self.api_key = api_key

    def get_current_weather(self, lat, lon):

        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key
        }

        response = requests.get(self.base_url, params=params)

        return response.json()


# openmeteo class
class OpenMeteoProvider(WeatherAbstract):

    base_url = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, lat, lon):

        params = {
            "longitude": lon,
            "latitude": lat,
            "current": "temperature_2m,relative_humidity_2m"
        }

        response = requests.get(self.base_url, params=params)

        return response.json()


# running the application

# Open-Meteo does not require an API key
provider = OpenMeteoProvider()

print(
    provider.get_current_weather(
        lat=52.52,
        lon=13.41
    )
)


# OpenWeather requires an API key
# provider = OpenWeatherProvider("YOUR_API_KEY")
# print(
#     provider.get_current_weather(
#         lat=52.52,
#         lon=13.41
#     )
# )