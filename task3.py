import json
from datetime import datetime
import pandas as pd
import os
import logging

# LOGGING SETUP
logging.basicConfig(
    filename='task3.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug('Script started.')

try:
    with open('task_2_and_3.json') as file:
        data = json.load(file)
    logging.debug('JSON file loaded successfully.')
except Exception as e:
    logging.error(f'Error loading JSON file: {e}')
    raise

df = pd.DataFrame(data)
logging.debug('DataFrame created from JSON data.')

# since date is not provided, i am generating current date here
df['Date'] = datetime.now().strftime('%Y-%m-%d')
logging.debug('Current date added to DataFrame: %s', df['Date'].head())

# determine season based on winter and summer values
df['Season'] = df.apply(lambda row: 'Winter' if row['winter'] == '1' and row['summer'] != '1'
                        else 'Summer' if row['summer'] == '1' and row['winter'] != '1'
                        else 'All Season', axis=1)
logging.debug('Season determined and added to DataFrame: %s', df['Season'].head())

# since tyre size is not provided, this is a hypothetical solution for tyre size
df['Tyre Size'] = df['width'] + '/' + 'R' + df['rim']
logging.debug('Tyre Size column created: %s', df['Tyre Size'].head())

# select and rename columns
df_output = df[['Date', 'manufacturer', 'pattern', 'Tyre Size', 'Season', 'tyre_class', 'rolling_resistance', 'wet_grip', 'noise_rating', 'price']]
df_output.columns = ['Date', 'Brand', 'Pattern', 'Tyre Size', 'Season', 'Class', 'Rolling Resistance', 'Wet Rating', 'Noise Rating', 'Price (£)']
logging.debug('Columns selected and renamed: %s', df_output.columns)

file_name = 'file.csv'


"""
THIS CHUNK GUIDES WHAT HAPPENS IF THE CSV FILE ALREADY EXISTS
"""
if os.path.exists(file_name):
    logging.debug(f'File {file_name} already exists.')
    while True:
        user_input = input(
            f"File '{file_name}' already exists. Enter '1' to overwrite or '0' to keep the existing file: ").strip()
        logging.debug(f'User input received: {user_input}')

        if user_input == "1":
            try:
                os.remove(file_name)
                logging.debug(f"Existing file '{file_name}' has been overwritten.")
                break
            except Exception as e:
                logging.error(f"Error removing file '{file_name}': {e}")
                raise
        elif user_input == "0":
            logging.debug(f"Existing file '{file_name}' was not overwritten. User chose to keep existing file.")
            print(f"Existing file '{file_name}' was not overwritten. Change the name of your file and try again!")
            exit()
        else:
            logging.warning("Invalid input provided for file overwrite decision.")
            print("Invalid input. Please enter '1' to overwrite or '0' to keep existing file.")
else:
    logging.debug(f'File {file_name} does not exist. Proceeding to create the file.')

# convert DataFrame to CSV
try:
    df_output.to_csv(file_name, encoding='utf-8', index=False)
    logging.debug(f"File '{file_name}' has been created and saved successfully.")
except Exception as e:
    logging.error(f"Error saving file '{file_name}': {e}")
    raise

logging.debug('Script completed.')
