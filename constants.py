WEATHER_CATEGORIES = {
    "good": [116, 113],
    "moody": [248, 143, 122, 119],
    "chill": [296, 293],
    "moderate": [374, 362, 332, 329, 320, 317, 311, 302, 299, 260, 185, 182, 179, 176],
    "fun": [368, 353, 326, 323, 266, 263],
    "bad": [392, 386, 377, 371, 365, 356, 350, 335, 314, 308, 305, 284, 281],
    "dangerous": [395, 389, 359, 338, 230, 227, 200],
}

WEATHER_VALENCE = {
    "good": [0.7, 1],
    "moody": [0.2, 0.5],
    "chill": [0.5, 0.7],
    "moderate": [0.4, 0.6],
    "fun": [0.8, 1],
    "bad": [0.3, 0.6],
    "dangerous": [0, 0.3],
}

WEATHER_CODES = {
    395: 'Moderate or heavy snow in area with thunder',
    392: 'Patchy light snow in area with thunder',
    389: 'Moderate or heavy rain in area with thunder',
    386: 'Patchy light rain in area with thunder',
    377: 'Moderate or heavy showers of ice pellets',
    374: 'Light showers of ice pellets',
    371: 'Moderate or heavy snow showers',
    368: 'Light snow showers',
    365: 'Moderate or heavy sleet showers',
    362: 'Light sleet showers',
    359: 'Torrential rain shower',
    356: 'Moderate or heavy rain shower',
    353: 'Light rain shower',
    350: 'Ice pellets',
    338: 'Heavy snow',
    335: 'Patchy heavy snow',
    332: 'Moderate snow',
    329: 'Patchy moderate snow',
    326: 'Light snow',
    323: 'Patchy light snow',
    320: 'Moderate or heavy sleet',
    317: 'Light sleet',
    314: 'Moderate or Heavy freezing rain',
    311: 'Light freezing rain',
    308: 'Heavy rain',
    305: 'Heavy rain at times',
    302: 'Moderate rain',
    299: 'Moderate rain at times',
    296: 'Light rain',
    293: 'Patchy light rain',
    284: 'Heavy freezing drizzle',
    281: 'Freezing drizzle',
    266: 'Light drizzle',
    263: 'Patchy light drizzle',
    260: 'Freezing fog',
    248: 'Fog',
    230: 'Blizzard',
    227: 'Blowing snow',
    200: 'Thundery outbreaks in nearby',
    185: 'Patchy freezing drizzle nearby',
    182: 'Patchy sleet nearby',
    179: 'Patchy snow nearby',
    176: 'Patchy rain nearby',
    143: 'Mist',
    122: 'Overcast',
    119: 'Cloudy',
    116: 'Partly Cloudy',
    113: 'Clear/Sunny'
}
