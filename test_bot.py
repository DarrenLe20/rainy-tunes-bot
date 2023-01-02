import unittest
import requests
import main
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()


class TestBot(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_get_current_date(self):
        self.assertEqual(main.get_current_date(),
                         date.today().strftime("%B %d, %Y"))

    def test_auth(self):
        self.assertIsNotNone(main.twitter_auth())
        self.assertIsNotNone(main.spotify_auth())

    def test_get_weather_fail(self):
        self.assertEqual(main.get_weather("aaaaaaa"),
                         ("Error: Could not get weather data", 0))

    def test_get_weather_success(self):
        WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
        req = requests.get(
            "http://api.weatherstack.com/current?access_key=" + WEATHERSTACK_API_KEY + "&query=New York")
        response = req.json()
        description = response['current']['weather_descriptions'][0]
        weather_code = response['current']['weather_code']
        msg = "New York (" + main.get_current_date() + "): " + description
        self.assertEqual(main.get_weather(), (msg, weather_code))
