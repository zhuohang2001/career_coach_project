import unittest
import pandas as pd
from src.load_data import CarparkDataLoader
from unittest.mock import patch, MagicMock
import os

class TestCarparkDataLoader(unittest.TestCase):

    def setUp(self):
        """Setup test files"""
        self.test_csv = "tests/test_data.csv"
        self.test_json = "tests/test_data.json"

        # Create sample CSV
        sample_data = pd.DataFrame({"car_park_no": ["A1", "B2"], "address": ["Blk 123", "Blk 456"]})
        sample_data.to_csv(self.test_csv, index=False)

        # Create sample JSON
        sample_json_data = {
            "items": [{
                "carpark_data": [
                    {"carpark_number": "A1", "carpark_info": [{"total_lots": "100", "lots_available": "50"}]}
                ]
            }]
        }
        with open(self.test_json, "w") as f:
            f.write(str(sample_json_data).replace("'", '"'))  # Convert to valid JSON format

    def test_load_valid_csv(self):
        """Test loading a valid CSV file"""
        df = CarparkDataLoader.load_csv(self.test_csv)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_load_missing_csv(self):
        """Test handling missing CSV file"""
        df = CarparkDataLoader.load_csv("missing_file.csv")
        self.assertIsNone(df)

    def test_load_valid_json(self):
        """Test loading valid JSON file"""
        data = CarparkDataLoader.load_json(json_path=self.test_json)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    @patch("requests.get")
    def test_api_error_handling(self, mock_get):
        """Test API failure handling"""
        mock_get.side_effect = Exception("API call failed")
        data = CarparkDataLoader.load_json(api_url="https://fake-api.com")
        self.assertEqual(data, [])

    def tearDown(self):
        """Clean up test files"""
        os.remove(self.test_csv)
        os.remove(self.test_json)

if __name__ == "__main__":
    unittest.main()
