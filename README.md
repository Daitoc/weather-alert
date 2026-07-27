# Weather Alert

A simple Python script that checks the rain forecast for tomorrow and alerts you whether you should expect rain or not, using the free Open-Meteo API.

## How it works

The script asks the user for a city name, uses the Open-Meteo Geocoding API to convert it into coordinates, then sends those coordinates to the Open-Meteo Weather API to retrieve the daily rain probability forecast. Finally, it prints a message telling you the chance of rain for tomorrow.


## Technologies used

- Python 3
- [Requests](https://docs.python-requests.org/) — to make HTTP calls to the API
- [Open-Meteo Weather API](https://open-meteo.com/) — free weather API, no API key required
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) — converts city names into coordinates


## How to run

1. Clone this repository:

git clone https://github.com/Daitoc/weather-alert.git

2. Install the required library:

pip install requests

3. Run the script:

python main.py


## Example output

Enter the name of your city: São Paulo
It shouldn't rain tomorrow 0%


## Next steps

- Send alerts via email or Telegram instead of just printing to the terminal
- Automate the script to run daily