from scripts.extract_restaurants import save_restaurant_details
from scripts.extract_events import extract_events
from scripts.analyse_ratings import analyze_ratings

if __name__ == "__main__":
    print("Starting Scenario 1 Processing...")

    # Extract and Save Restaurant Details
    save_restaurant_details() 

    # Extract Events for April 2019
    extract_events()

    # Analyze Ratings
    analyze_ratings()

    print("Scenario 1 processing completed!")
