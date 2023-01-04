![Workflow Status](https://github.com/DarrenLe20/rainy-tunes-bot/actions//workflows/test.yml/badge.svg?event=push)

# Rainy Tunes Bot

Music recommendation Twitter bot

Twitter: https://twitter.com/rainytunesbot

## How it works

The bot is written in Python and uses [Tweepy](https://www.tweepy.org/) library to interact with the Twitter API, [tekore](https://tekore.readthedocs.io/en/stable/) library to interact with the Spotify API, and [Weatherstack](https://weatherstack.com/) API to get the weather data of a location (default is New York, USA). The bot will analyze the weather data and recommend a song based on the weather conditions through tweets. Followers will also receive a direct message everyday with a recommended song based on the weather their local location extracted from Twitter Bio.

## Running the bot locally

1. Clone the repository
2. Create a virtual environment and install the dependencies fromn the requirements.txt file

      ```pip install -r requirements.txt```

3. Create a Twitter developer account and create a new app [here](https://developer.twitter.com/)
4. Generate the necessery keys and tokens for the app
5. Apply for elevated access to the Twitter API
6. Create a Spotify developer account and create a new app [here](https://developer.spotify.com/dashboard/)
7. Create a Weatherstack account and generate an API key [here](https://weatherstack.com/)
8. Create a .env file with the following environment variables

      ```TWITTER_API="your_twitter_api_key"```

      ```TWITTER_SECRET="your_twitter_api_secret_key"```

      ```ACCESS="your_twitter_access_token"```

      ```ACCESS_SECRET="your_twitter_access_secret_token"```

      ```SPOTIFY_ID="your_spotify_key"```

      ```SPOTIFY_ID_SECRET="your_spotify_secret_key"```

      ```WEATHERSTACK_API_KEY="your_weatherstack_key"```

9. Run the main.py file

      ```python main.py```

## Automation

The bot is automated using GitHub Actions. The test workflow is triggered every time a commit is pushed to the repository. The tweet workflow is triggered manually or at 9AM and 9PM everyday.

## Author

[Darren Le](https://github.com/DarrenLe20)
