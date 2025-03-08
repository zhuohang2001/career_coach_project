import pandas as pd
from utils import load_restaurant_data, load_country_codes
from config import RESTAURANT_JSON, COUNTRY_CODE_XLSX, RESTAURANT_CSV

def extract_restaurant_details():
    """
    Extracts restaurant details from JSON data and maps country codes.

    - Loads country codes from an Excel file.
    - Reads restaurant data from JSON.
    - Extracts and structures essential information.

    Returns:
        pd.DataFrame: Processed restaurant details.
    """
    try:
        country_mapping = load_country_codes(COUNTRY_CODE_XLSX)
        restaurant_data = load_restaurant_data(RESTAURANT_JSON)

        extracted_data = []
        for record in restaurant_data[0]["restaurants"]:
            details = record["restaurant"]
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
    
    except FileNotFoundError:
        print(f"Error: Missing file '{COUNTRY_CODE_XLSX}' or '{RESTAURANT_JSON}'.")
        return pd.DataFrame()  # Return empty DataFrame for safety
    except Exception as e:
        print(f"Unexpected error in extracting restaurant details: {e}")
        return pd.DataFrame()

def save_restaurant_details():
    """
    Extracts and saves restaurant data to CSV.

    - Calls `extract_restaurant_details()`.
    - Saves processed data into `RESTAURANT_CSV`.
    """
    df = extract_restaurant_details()
    if df.empty:
        print("No data extracted. Skipping CSV save.")
        return
    
    df.fillna("N/A", inplace=True)
    df.to_csv(RESTAURANT_CSV, index=False)
    print(f"Restaurant details successfully stored in {RESTAURANT_CSV}")

if __name__ == "__main__":
    save_restaurant_details()
