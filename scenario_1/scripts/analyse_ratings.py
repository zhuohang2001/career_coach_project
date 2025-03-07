import pandas as pd
from config import RESTAURANT_CSV, RATING_THRESHOLDS

def categorize_rating(rating):
    """Categorize rating based on predefined thresholds."""
    if rating is None:  # Handle missing values
        return "NA"
    
    try:
        rating = float(rating)  # Convert to float safely
    except ValueError:
        return "NA"  # Handle unexpected values

    for category, threshold in RATING_THRESHOLDS.items():
        if rating >= threshold:
            return category

    return "NA"


def analyze_ratings():
    """Load restaurant details, categorize ratings, and update CSV."""
    df = pd.read_csv(RESTAURANT_CSV)
    df["Rating Category"] = df["Rating"].apply(categorize_rating)
    df.to_csv(RESTAURANT_CSV, index=False)
    print("Updated restaurant ratings with categories.")

if __name__ == "__main__":
    analyze_ratings()
