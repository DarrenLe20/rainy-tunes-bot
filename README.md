# Rainy Tunes Bot

Music recommendation Twitter bot

## How it works

The bot is written in Python and uses [Tweepy](https://www.tweepy.org/) library to interact with the Twitter API, [tekore](https://tekore.readthedocs.io/en/stable/) library to interact with the Spotify API, and [Weatherstack](https://weatherstack.com/) API to get the weather data of a location (default is New York, USA). The bot will analyze the weather data and recommend a song based on the weather conditions through tweets. Followers will also receive a direct message everyday with a recommended song based on their local location.

## Running the bot locally

1. Clone the repository
2. Create a virtual environment and install the dependencies fromn the requirements.txt file

      ```pip install -r requirements.txt```

3. Create a Twitter developer account and create a new app [here](https://developer.twitter.com/)
4. Generate the necessery keys and tokens for the app
5. Apply for elevated access to the Twitter API
6. Create a Spotify developer account and create a new app [here](https://developer.spotify.com/dashboard/)
7. Create a .env file with the following environment variables

      ```TWITTER_API="your_twitter_api_key"```

      ```TWITTER_SECRET="your_twitter_api_secret_key"```

      ```ACCESS="your_twitter_access_token"```

      ```ACCESS_SECRET="your_twitter_access_secret_token"```

      ```SPOTIFY_ID="your_spotify_key"```

      ```SPOTIFY_ID_SECRET="your_spotify_secret_key"```

8. Run the main.py file

      ```python main.py```

## Automation

The bot is automated using GitHub Actions. The workflow is triggered every time a commit is pushed to the repository or at 9AM everyday.

## Author

[Darren Le](https://github.com/DarrenLe20)
