from urllib import parse, request
from dotenv import load_dotenv
import requests
import time
import os
import tekore as tk
import tweepy as tp
from datetime import date

load_dotenv()

ERROR = False
tracks_data = {"id": [], "genre": [], "track_name": [], "artist_name": [],
               "valence": [], "url": []}
default_location = "New York"


def get_current_date():
    return date.today().strftime("%B %d, %Y")


def get_weather():
    WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
    try:
        req = requests.get(
            "http://api.weatherstack.com/current?access_key=" + WEATHERSTACK_API_KEY + "&query=" + default_location)
        response = req.json()
        description = response['current']['weather_descriptions'][0]
        weather_code = response['current']['weather_code']
        msg = default_location + \
            " (" + get_current_date() + "): " + description
        return msg, weather_code
    except:
        ERROR = True


# Authenticate to Twitter
def twitter_auth():
    auth = tp.OAuth1UserHandler(
        os.getenv("TWITTER_API"), os.getenv("TWITTER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS"), os.getenv("ACCESS_SECRET"))
    api = tp.API(auth)
    return api


def authorize_spotify():
    CLIENT_ID = os.getenv("SPOTIFY_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_ID_SECRET")
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)


def get_data(track):
    tracks_data["id"].append(track.id)
    tracks_data["genre"].append(track.genre)
    tracks_data["track_name"].append(track.name)
    artists = [artist.name for artist in track.artists]
    tracks_data["artist_name"].append(', '.join(artists))
    tracks_data["valence"].append(track.valence)
    tracks_data["url"].append(track.external_urls['spotify'])


def get_all_tracks():
    sp = authorize_spotify()
    genres = sp.recommendation_genre_seeds()
    for genre in genres:
        # 100 recommended tracks per genre
        rec = sp.recommendations(genres=[genre], limit=100)
        # add tracks to tracks_data
        for track in rec.tracks:
            get_data(track)
        time.sleep(0.5)


def recommend(weather_code):
    print(weather_code)


def tweet(api):
    if ERROR == False:
        msg, weather_code = get_weather()
        api.update_status(msg)
        recommend(weather_code)
        msg_follower(api, msg)


def msg_follower(api, msg):
    followers = api.get_follower_ids()
    for follower in followers:
        api.send_direct_message(
            follower, msg)


if __name__ == "__main__":
    api = twitter_auth()
    tweet(api)
    # get_all_tracks()
