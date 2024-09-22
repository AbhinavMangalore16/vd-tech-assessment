import csv
import os
import pandas as pd
import re


def email_valid(email):
    return re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email) is not None

def data_cleaning(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.drop_duplicates(subset='user_id')
    df = df[df['email'].apply(email_valid)]
    df = df.to_csv(output_file, index=False)
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, 'files', 'data_unclean.csv')
output_file = os.path.join(current_dir, 'files', 'data_cleaned.csv')

data_cleaning(input_file, output_file)