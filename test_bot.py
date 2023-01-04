import unittest
import requests
import main
import constants
from datetime import date
import os
from dotenv import load_dotenv
import random

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
        self.assertIsNotNone(main.tracks_data["id"])
        self.assertIsNotNone(main.tracks_data["track_name"])
        self.assertIsNotNone(main.tracks_data["valence"])
        self.assertIsNotNone(main.tracks_data["url"])
