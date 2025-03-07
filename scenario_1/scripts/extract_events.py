import pandas as pd
from utils import load_restaurant_data
from config import RESTAURANT_JSON, EVENTS_CSV

def extract_events():
    """Extract events occurring in April 2019 and save to CSV."""
    restaurant_data = load_restaurant_data(RESTAURANT_JSON)
    
    event_list = []
    restaurants = restaurant_data[0]["restaurants"]
    for entry in restaurants:
        rest = entry["restaurant"]
        if "zomato_events" in rest:
            for event in rest["zomato_events"]:
                evt = event["event"]
                if "2019-04" in evt["start_date"] or "2019-04" in evt["end_date"]:
                    event_list.append({
                        "Event Id": evt["event_id"],
                        "Restaurant Id": rest["id"],
                        "Name": rest["name"],
                        "Photo URL": evt["photos"][0]["photo"]["url"] if evt["photos"] else "NA",
                        "Title": evt["title"],
                        "Start Date": evt["start_date"],
                        "End Date": evt["end_date"]
                    })
    
    df = pd.DataFrame(event_list)
    df.fillna("NA", inplace=True)
    df.to_csv(EVENTS_CSV, index=False)
    print(f"Saved event details to {EVENTS_CSV}")

if __name__ == "__main__":
    extract_events()
