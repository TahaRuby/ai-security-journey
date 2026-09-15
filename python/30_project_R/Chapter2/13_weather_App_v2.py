# import and global variables

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window

import requests


# window size

Window.size = (450, 550)


# Open-Meteo API provider

class OpenMeteoProvider:

    # API URLs

    weather_url = "https://api.open-meteo.com/v1/forecast"
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"


    # function for finding city coordinates

    def get_city_coordinates(self, city):

        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = requests.get(
            self.geocoding_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()


        # check if the city was found

        if "results" not in data or not data["results"]:
            return None


        city_data = data["results"][0]


        return {
            "name": city_data["name"],
            "country": city_data.get("country", ""),
            "latitude": city_data["latitude"],
            "longitude": city_data["longitude"]
        }


    # function for getting current weather

    def get_current_weather(self, latitude, longitude):

        params = {
            "latitude": latitude,
            "longitude": longitude,

            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "wind_speed_10m,"
                "weather_code"
            ),

            "temperature_unit": "celsius",

            "wind_speed_unit": "kmh"
        }


        response = requests.get(
            self.weather_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()


        # get current weather data

        current = data["current"]


        return {
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"],
            "weather_code": current["weather_code"]
        }


# main application

class WeatherGUIApp(App):


    # build the application UI

    def build(self):

        # create main layout

        main_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )


        # application title

        title_label = Label(
            text="Weather App",
            font_size=32,
            size_hint_y=None,
            height=60
        )


        # city input

        self.city_entry = TextInput(
            hint_text="Enter city name",
            multiline=False,
            size_hint_y=None,
            height=50
        )


        # search button

        search_button = Button(
            text="Get Weather",
            size_hint_y=None,
            height=50
        )


        search_button.bind(
            on_press=self.fetch_weather
        )


        # temperature unit button

        self.unit_button = Button(
            text="Unit: °C",
            size_hint_y=None,
            height=45
        )


        self.unit_button.bind(
            on_press=self.change_unit
        )


        # result label

        self.result_label = Label(
            text="Enter a city to get weather information.",
            font_size=20
        )


        # status label

        self.status_label = Label(
            text="Ready",
            font_size=16,
            size_hint_y=None,
            height=40
        )


        # add widgets to main layout

        main_layout.add_widget(
            title_label
        )

        main_layout.add_widget(
            self.city_entry
        )

        main_layout.add_widget(
            search_button
        )

        main_layout.add_widget(
            self.unit_button
        )

        main_layout.add_widget(
            self.result_label
        )

        main_layout.add_widget(
            self.status_label
        )


        # create API provider

        self.provider = OpenMeteoProvider()


        # default temperature unit

        self.use_fahrenheit = False


        # save last weather data

        self.last_weather = None


        return main_layout


    # function for getting weather data

    def fetch_weather(self, instance):

        # get city name from input

        city = self.city_entry.text.strip()


        # check empty input

        if city == "":

            self.status_label.text = (
                "Please enter a city name."
            )

            return


        # show loading message

        self.status_label.text = "Fetching weather..."

        self.result_label.text = "Please wait..."


        try:

            # find city coordinates

            city_data = self.provider.get_city_coordinates(
                city
            )


            # check if city exists

            if city_data is None:

                self.status_label.text = (
                    "City not found."
                )

                self.result_label.text = (
                    "Please check the city name."
                )

                return


            # get weather using coordinates

            weather_data = (
                self.provider.get_current_weather(
                    city_data["latitude"],
                    city_data["longitude"]
                )
            )


            # save weather data

            self.last_weather = {
                "city": city_data,
                "weather": weather_data
            }


            # display weather information

            self.show_weather()


        except requests.exceptions.RequestException:

            # handle internet/API errors

            self.status_label.text = (
                "Connection error."
            )

            self.result_label.text = (
                "Could not connect to weather API."
            )


        except (KeyError, ValueError):

            # handle invalid API data

            self.status_label.text = (
                "Invalid weather data."
            )

            self.result_label.text = (
                "Something went wrong with the API response."
            )


    # function for showing weather information

    def show_weather(self):

        # make sure weather data exists

        if self.last_weather is None:
            return


        city_data = self.last_weather["city"]
        weather_data = self.last_weather["weather"]


        # get city information

        city_name = city_data["name"]
        country = city_data["country"]


        # get weather information

        temperature = weather_data["temperature"]
        humidity = weather_data["humidity"]
        wind_speed = weather_data["wind_speed"]
        weather_code = weather_data["weather_code"]


        # convert temperature if Fahrenheit is selected

        if self.use_fahrenheit:

            temperature = (
                temperature * 9 / 5
            ) + 32

            temperature_text = (
                f"{temperature:.1f} °F"
            )

        else:

            temperature_text = (
                f"{temperature:.1f} °C"
            )


        # convert weather code to readable text

        weather_description = (
            self.get_weather_description(
                weather_code
            )
        )


        # create result text

        result = (
            f"{city_name}, {country}\n\n"
            f"Temperature: {temperature_text}\n"
            f"Condition: {weather_description}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} km/h"
        )


        # show result

        self.result_label.text = result

        self.status_label.text = "Weather updated."


    # function for changing Celsius/Fahrenheit

    def change_unit(self, instance):

        self.use_fahrenheit = (
            not self.use_fahrenheit
        )


        # update button text

        if self.use_fahrenheit:

            self.unit_button.text = "Unit: °F"

        else:

            self.unit_button.text = "Unit: °C"


        # refresh weather information

        if self.last_weather is not None:

            self.show_weather()


    # function for converting weather codes

    def get_weather_description(self, weather_code):

        weather_codes = {

            0: "Clear sky",

            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",

            45: "Fog",
            48: "Depositing rime fog",

            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",

            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",

            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",

            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",

            95: "Thunderstorm",

            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }


        # return description

        return weather_codes.get(
            weather_code,
            "Unknown weather"
        )


# run application

if __name__ == "__main__":

    WeatherGUIApp().run()