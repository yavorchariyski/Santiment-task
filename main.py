import json
import logging
import sqlite3
import time
from datetime import datetime

import san
import schedule

logging.basicConfig(level=logging.DEBUG)

# Load the JSON file
with open('config.json') as f:
    config = json.load(f)

# Access the variables
api_key = config['SANTIMENT_API_KEY']

# Get the current date
today = datetime.utcnow().date()

# Convert the date object to a string
today_string = today.strftime('%Y-%m-%d')


def get_metrics():
    # Set your API key (not used for this test case)
    san.ApiConfig.api_key = api_key
    # Make the GET request to the Santiment API
    response = san.get_many(
        "price_usd",
        slugs=["bitcoin", "ethereum"],
        from_date=today_string,
        to_date=today_string,
        interval="1h"
    )
    # Handle the response
    if not response.empty:
        # get the data in pandas dataframe format
        df = response
        # Connect to SQLite database
        with sqlite3.connect('metrics.db') as conn:
            # Store the data in a table
            df.to_sql('metrics', conn, if_exists='append', index=False)
            logging.info('Data stored in the table')
    else:
        logging.warning("Failed to retrieve data. Empty response.")


# Schedule the script to run once an hour
schedule.every(1).hour.do(get_metrics)

while True:
    schedule.run_pending()
    time.sleep(1)
