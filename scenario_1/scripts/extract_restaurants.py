import pandas as pd
from utils import load_restaurant_data, load_country_codes
from config import RESTAURANT_JSON, COUNTRY_CODE_XLSX, RESTAURANT_CSV

def extract_restaurant_details():
    """Extract relevant restaurant details from JSON."""
    country_mapping = load_country_codes(COUNTRY_CODE_XLSX)
    restaurant_data = load_restaurant_data(RESTAURANT_JSON)

    extracted_data = []
    restaurants = restaurant_data[0]["restaurants"]
    for record in restaurants:  
        details = record["restaurant"]  # Extract actual restaurant data
        location = details.get("location", {})
        user_rating = details.get("user_rating", {})

        extracted_data.append({
            "Restaurant_Id": details.get("id", "N/A"),
            "Name": details.get("name", "N/A"),
            "Country": country_mapping.get(location.get("country_id", ""), "Unknown"),
            "City": location.get("city", "N/A"),
            "Rating": user_rating.get("aggregate_rating", "N/A"),
            "Cuisines": details.get("cuisines", "N/A")
        })
    
    return pd.DataFrame(extracted_data)

def save_restaurant_details():
    """Extract and save restaurant data to CSV."""
    df = extract_restaurant_details()
    df.fillna("N/A", inplace=True)
    df.to_csv(RESTAURANT_CSV, index=False)
    print(f"Restaurant details successfully stored in {RESTAURANT_CSV}")

if __name__ == "__main__":
    save_restaurant_details()
