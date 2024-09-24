import csv
import os
import pandas as pd
import re
import logging
logging.basicConfig(
    filename='data_cleaning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def email_valid(email):
    logging.info(f"Validating email: {email}")
    return re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email) is not None

def data_cleaning(input_file, output_file):
    try:
        logging.info(f"Reading input file: {input_file}")
        df = pd.read_csv(input_file)
        df = df.drop_duplicates(subset='user_id')
        logging.info(f"Data after removing duplicates: {len(df)} rows")
        df = df[df['email'].apply(email_valid)]
        df.to_csv(output_file, index=False)
        logging.info(f"Data saved to output file: {output_file}")
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, 'files', 'data_unclean.csv')
output_file = os.path.join(current_dir, 'files', 'data_cleaned.csv')

data_cleaning(input_file, output_file)
