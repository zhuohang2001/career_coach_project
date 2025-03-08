import unittest
from unittest.mock import patch
from app import app

class TestRestaurantProcessingAPI(unittest.TestCase):
    """Tests for the Flask API endpoints in app.py"""

    def setUp(self):
        """Set up test client before each test"""
        self.client = app.test_client()
        self.client.testing = True

    @patch("app.save_restaurant_details") 
    @patch("app.extract_events")          
    @patch("app.analyze_ratings")  
    def test_process_all(self, mock_analyze_ratings, mock_extract_events, mock_save_restaurants):
        """Test the /process-all endpoint"""

        # Mock function calls to avoid executing actual logic
        mock_save_restaurants.return_value = None
        mock_extract_events.return_value = None
        mock_analyze_ratings.return_value = None

        # Make a request to the /process-all endpoint
        response = self.client.post("/process-all")

        # Validate response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "All restaurant data processing completed successfully!"})

        # Ensure all functions were called once
        mock_save_restaurants.assert_called_once()
        mock_extract_events.assert_called_once()
        mock_analyze_ratings.assert_called_once()

    def test_home_endpoint(self):
        """Test the root '/' endpoint"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Restaurant Data Processing API is running!"})

if __name__ == "__main__":
    unittest.main()
