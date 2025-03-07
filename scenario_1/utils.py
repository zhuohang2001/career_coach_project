import json
import pandas as pd

def load_country_codes(filepath):
    """Load country codes from an Excel file into a dictionary."""
    df = pd.read_excel(filepath)
    return dict(zip(df["Country Code"], df["Country"]))

def load_restaurant_data(filepath):
    """Load restaurant data from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)
