import pandas as pd
from config import RESTAURANT_CSV, RATING_THRESHOLDS

def categorize_rating(rating):
    """
    Categorize restaurant rating based on predefined thresholds.

    - Converts rating to float safely, handling missing or invalid values.
    - Uses predefined rating categories from `config.py`.
    
    Args:
        rating (float | str | None): Raw rating from the dataset.

    Returns:
        str: Corresponding category (e.g., "Excellent", "Good", "NA").
    """
    if rating is None: 
        return "NA"
    
    try:
        rating = float(rating)
    except ValueError:
        return "NA"  # Return NA if rating is not a valid number

    for category, threshold in RATING_THRESHOLDS.items():
        if rating >= threshold:
            return category

    return "NA"  # Fallback for unexpected cases

def analyze_ratings():
    """
    Loads restaurant details, categorizes ratings, and updates the dataset.

    - Reads the restaurant dataset from `RESTAURANT_CSV`.
    - Applies `categorize_rating()` to classify each rating.
    - Saves the updated dataset with the new rating category.
    """
    try:
        df = pd.read_csv(RESTAURANT_CSV)
        df["Rating Category"] = df["Rating"].apply(categorize_rating)
        df.to_csv(RESTAURANT_CSV, index=False)
        print("Updated restaurant ratings with categories.")
    except FileNotFoundError:
        print(f"Error: File '{RESTAURANT_CSV}' not found.")
    except Exception as e:
        print(f"Unexpected error while processing ratings: {e}")

if __name__ == "__main__":
    analyze_ratings()
