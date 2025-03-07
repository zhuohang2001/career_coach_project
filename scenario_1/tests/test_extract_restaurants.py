import pytest
import pandas as pd
from scripts.extract_restaurants import extract_restaurant_details, save_restaurant_details
from config import RESTAURANT_CSV

@pytest.fixture
def mock_restaurant_data():
    """Simulated restaurant data."""
    return [{
        "restaurant": {
            "id": "18649486",
            "name": "Mock Diner",
            "location": {"country_id": 1, "city": "Mock City"},
            "user_rating": {"aggregate_rating": 4.5},
            "cuisines": "Italian, Chinese"
        }
    }]

def test_extract_restaurant_details(mocker, mock_restaurant_data):
    """Ensure restaurant details are extracted properly."""
    mocker.patch("utils.load_restaurant_data", return_value=[{"restaurants": mock_restaurant_data}])
    mocker.patch("utils.load_country_codes", return_value={1: "Mockland"})

    df = extract_restaurant_details()
    
    assert not df.empty
    assert df.iloc[0]["Restaurant_Id"] == "18649486"
    assert df.iloc[0]["Country"] == "India"
    assert df.iloc[0]["City"] == "Gurgaon"

def test_save_restaurant_details(mocker):
    """Ensure restaurant data is saved to CSV."""
    mocker.patch("scripts.extract_restaurants.extract_restaurant_details", return_value=pd.DataFrame({
        "Restaurant_Id": ["18649486"],
        "Name": ["Mock Diner"],
        "Country": ["Mockland"],
        "City": ["Mock City"],
        "Rating": [4.5],
        "Cuisines": ["Italian, Chinese"]
    }))
    mocker.patch("pandas.DataFrame.to_csv")  # Prevent file write

    save_restaurant_details()
