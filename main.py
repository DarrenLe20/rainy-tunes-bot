from urllib import parse, request
from dotenv import load_dotenv
import requests
import json
import os
import tekore as tk
import tweepy as tp
from datetime import date

load_dotenv()

ERROR = False


def get_current_date():
    return date.today().strftime("%B %d, %Y")


def get_weather():
    WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")
    try:
        req = requests.get(
            "http://api.weatherstack.com/current?access_key=" + WEATHERSTACK_API_KEY + "&query=New York")
        response = req.json()
        description = response['current']['weather_descriptions'][0]
        temperature = response['current']['temperature']
        # precipitation = response['current']['precip']
        # humidity = response['current']['humidity']
        # visibility = response['current']['visibility']
        # wind_speed = response['current']['wind_speed']
        # feels_like = response['current']['feelslike']
        msg = "New York (" + get_current_date() + "): " + \
            description + ", " + str(temperature) + "°C"
        return msg
    except:
        ERROR = True

# Authenticate to Twitter


def api_auth():
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


def get_all_tracks():
    sp = authorize_spotify()
    genres = sp.recommendation_genre_seeds()
    for genre in genres:
        rec = sp.recommendations(genres=[genre], limit=1)


def tweet(api):
    if ERROR == False:
        msg = get_weather()
        # msg_follower(api)


# def msg_follower(api):
#     followers = api.get_follower_ids()
#     for follower in followers:
#         api.send_direct_message(
#             follower, "The weather in your area on " + get_current_date() + " is: ")


if __name__ == "__main__":
    # api = api_auth()
    # tweet(api)
    get_all_tracks()
