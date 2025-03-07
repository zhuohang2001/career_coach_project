import pytest
import pandas as pd
from scripts.analyse_ratings import analyze_ratings, categorize_rating
from config import RESTAURANT_CSV, RATING_THRESHOLDS

@pytest.mark.parametrize("rating,expected_category", [
    (4.8, "Excellent"),
    (4.2, "Very Good"),
    (3.6, "Good"),
    (3.0, "Average"),
    (2.5, "Poor"),
    (None, "NA"),  # Handles missing values
])
def test_categorize_rating(rating, expected_category):
    """Ensure ratings are categorized correctly."""
    assert categorize_rating(rating) == expected_category

def test_analyze_ratings(mocker):
    """Check if restaurant CSV updates with rating categories."""
    mock_df = pd.DataFrame({
        "Restaurant_Id": [1, 2, 3],
        "Rating": [4.6, 3.4, 2.0]
    })

    mocker.patch("pandas.read_csv", return_value=mock_df)
    mocker.patch("pandas.DataFrame.to_csv")  # Prevent actual file write

    analyze_ratings()
    
    assert "Rating Category" in mock_df.columns
    assert mock_df["Rating Category"].tolist() == ["Excellent", "Average", "Poor"]
