# Weather Alert

A simple Python script that checks the rain forecast for tomorrow and alerts you whether you should expect rain or not, using the free Open-Meteo API.

## How it works

The script sends a request to the Open-Meteo API with a given location (latitude and longitude), retrieves the daily rain probability forecast, and prints a message telling you the chance of rain for the next day.

## Technologies used

- Python 3
- [Requests](https://docs.python-requests.org/) — to make HTTP calls to the API
- [Open-Meteo API](https://open-meteo.com/) — free weather API, no API key required

## How to run

1. Clone this repository:

git clone https://github.com/Daitoc/weather-alert.git

2. Install the required library:

pip install requests

3. Run the script:

python main.py


## Example output

It shouldn't rain tomorrow 0%


## Next steps

- Allow the user to input any city instead of fixed coordinates
- Send alerts via email or Telegram instead of just printing to the terminal
- Automate the script to run daily