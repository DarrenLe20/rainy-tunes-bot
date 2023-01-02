# Rainy Tunes Bot

Music recommendation Twitter bot

## How it works

The bot is written in Python and uses [Tweepy](https://www.tweepy.org/) library to interact with the Twitter API, [tekore](https://tekore.readthedocs.io/en/stable/) library to interact with the Spotify API, and [Weatherstack](https://weatherstack.com/) API to get the weather data of a location (default is New York, USA). The bot will analyze the weather data and recommend a song based on the weather conditions through tweets. Followers will also receive a direct message everyday with a recommended song based on their local location.
