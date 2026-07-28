# Weather Alert

A simple Python script that checks the rain forecast for tomorrow and alerts you whether you should expect rain or not, using the free Open-Meteo API.

## How it works

The script asks the user for a city name, uses the Open-Meteo Geocoding API to convert it into coordinates, then sends those coordinates to the Open-Meteo Weather API to retrieve the daily rain probability forecast. Finally, it sends an email letting you know the chance of rain for tomorrow.

## Technologies used

- Python 3
- [Requests](https://docs.python-requests.org/) — to make HTTP calls to the API
- [Open-Meteo Weather API](https://open-meteo.com/) — free weather API, no API key required
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) — converts city names into coordinates
- `smtplib` (built into Python) — to send the email alert
- [python-dotenv](https://pypi.org/project/python-dotenv/) — to safely load email credentials from a local `.env` file

## How to run

1. Clone this repository:

git clone https://github.com/Daitoc/weather-alert.git

2. Install the required libraries:

pip install requests python-dotenv

3. Create a `.env` file in the project folder with your Gmail credentials:

EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your16digitapppassword

⚠️ You'll need to generate a Gmail [App Password](https://myaccount.google.com/apppasswords) (requires 2-step verification enabled). Never commit your `.env` file.

4. Run the script:

python main.py

## Example output

Enter the name of your city: São Paulo
(you'll receive an email letting you know the chance of rain for tomorrow)

## Next steps

- Send alerts via Telegram as an alternative to email
- Automate the script to run daily