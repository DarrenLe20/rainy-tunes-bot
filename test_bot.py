import unittest
import requests
import main
from datetime import date
from dotenv import load_dotenv
import os
import random
import constants

load_dotenv()
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")


class TestBot(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_get_current_date(self):
        self.assertEqual(main.get_current_date(),
                         date.today().strftime("%B %d, %Y"))

    def test_auth(self):
        self.assertIsNotNone(main.twitter_auth())
        self.assertIsNotNone(main.spotify_auth())

    def test_get_weather(self):
        response = requests.get(
            "http://api.weatherstack.com/current?access_key=" + WEATHERSTACK_API_KEY + "&query=New York")
        assert response.status_code == 200

    def test_get_recommendations(self):
        sp = main.spotify_auth()
        genre = random.choice(constants.GENRES)
        self.assertIsNotNone(constants.GENRES)
        self.assertIsNotNone(sp.recommendations(genres=[genre], limit=1))

    def test_get_all_tracks(self):
        sp = main.spotify_auth()
        genre = random.choice(constants.GENRES)
        rec = sp.recommendations(genres=[genre], limit=1)
        main.get_data(rec.tracks[0], sp)
        self.assertIsNotNone(main.tracks_data["valence"])
        self.assertIsNotNone(main.tracks_data["url"])
