import pytest
import pandas as pd
from scripts.extract_events import extract_events
from config import EVENTS_CSV

@pytest.fixture
def sample_event_data():
    """Simulated restaurant data with events."""
    return [{
        "restaurant": {
            "id": "1001",
            "name": "Test Restaurant",
            "zomato_events": [
                {"event": {"event_id": 123, "start_date": "2019-04-10", "end_date": "2019-04-15", "title": "Spring Fest"}},
                {"event": {"event_id": 124, "start_date": "2019-03-10", "end_date": "2019-03-20", "title": "Old Fest"}}
            ]
        }
    }]

def test_extract_events(mocker, sample_event_data):
    """Ensure only April 2019 events are extracted."""
    mocker.patch("utils.load_restaurant_data", return_value=[{"restaurants": sample_event_data}])
    mocker.patch("pandas.DataFrame.to_csv")  # Avoid actual file write

    extract_events()
    
    df = pd.DataFrame(sample_event_data)
    assert not df.empty
    assert df.iloc[0]["restaurant"]["zomato_events"][0]["event"]["title"] == "Spring Fest"
