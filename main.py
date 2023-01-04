from dotenv import load_dotenv
import requests
import time
import os
import tekore as tk
import tweepy as tp
from datetime import date
import constants
import random

load_dotenv()

ERROR = False
tracks_data = {"valence": [], "url": []}
default_location = "New York"


def get_current_date():
    return date.today().strftime("%B %d, %Y")


def get_weather(location=default_location):
    WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
    try:
        req = requests.get(
            "http://api.weatherstack.com/current?access_key=" + WEATHERSTACK_API_KEY + "&query=" + location)
        response = req.json()
        description = response['current']['weather_descriptions'][0]
        weather_code = response['current']['weather_code']
        time = response['current']['observation_time']
        msg = default_location + \
            " (" + get_current_date() + " - " + time + "): " + description
        return msg, weather_code
    except:
        ERROR = True
        msg = "Error: Could not get weather data"
        return msg, 0


# Authenticate to Twitter
def twitter_auth():
    auth = tp.OAuth1UserHandler(
        os.getenv("TWITTER_API"), os.getenv("TWITTER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS"), os.getenv("ACCESS_SECRET"))
    api = tp.API(auth)
    return api


# Authenticate to Spotify
def spotify_auth():
    CLIENT_ID = os.getenv("SPOTIFY_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_ID_SECRET")
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)


def get_data(track, sp):
    valence = sp.track_audio_features(track.id).valence
    tracks_data["valence"].append(valence)
    tracks_data["url"].append(track.external_urls['spotify'])


def get_all_tracks():
    sp = spotify_auth()
    genres = constants.GENRES
    genre = random.choice(genres)
    # 100 recommended tracks per genre
    rec = sp.recommendations(genres=[genre], limit=50)
    # add tracks to tracks_data
    for track in rec.tracks:
        get_data(track, sp)


def get_cond(weather_code):
    for key, val in constants.WEATHER_CATEGORIES.items():
        if (weather_code in val):
            return key


def recommend(weather_code):
    cond = get_cond(weather_code)
    min = constants.WEATHER_VALENCE[cond][0]
    max = constants.WEATHER_VALENCE[cond][1]
    # find a track that matches the weather condition
    for i in range(len(tracks_data["valence"])):
        if (tracks_data["valence"][i] >= min and tracks_data["valence"][i] <= max):
            return tracks_data["url"][i]


def tweet(api):
    if ERROR == False:
        msg, weather_code = get_weather()
        get_all_tracks()
        song_url = recommend(weather_code)
        msg += "\n" + song_url
        api.update_status(msg)
        msg_follower(api, msg)


def get_location(api, user_id):
    try:
        location = api.get_user(user_id).location
        if location == "":
            location = default_location
        return location
    except:
        return default_location


def msg_follower(api, default_msg):
    followers = api.get_follower_ids()
    for follower in followers:
        location = get_location(api, follower)
        if location == default_location:
            msg = default_msg
        else:
            msg, weather_code = get_weather(location=location)
            song_url = recommend(weather_code)
            msg += "\n" + song_url
        api.send_direct_message(follower, msg)


if __name__ == "__main__":
    api = twitter_auth()
    tweet(api)
