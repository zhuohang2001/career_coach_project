import unittest
import pandas as pd
from src.process_data import CarparkDataProcessor

class TestCarparkDataProcessor(unittest.TestCase):

    def setUp(self):
        """Create sample static and real-time data for testing"""
        self.static_data = pd.DataFrame({
            "car_park_no": ["A1", "B2"],
            "address": ["Blk 123", "Blk 456"],
            "type_of_parking_system": ["Electronic", "Coupon"]
        })

        self.realtime_data = [
            {"carpark_number": "A1", "carpark_info": [{"total_lots": "100", "lots_available": "50"}], "update_datetime": "2025-03-07T17:06:52"},
            {"carpark_number": "B2", "carpark_info": [{"total_lots": "200", "lots_available": "100"}], "update_datetime": "2025-03-07T17:06:52"}
        ]

    def test_format_realtime_data(self):
        """Test converting JSON data to DataFrame"""
        df = CarparkDataProcessor.format_realtime_data(self.realtime_data)
        self.assertIn("carpark_number", df.columns)
        self.assertIn("total_lots", df.columns)
        self.assertIn("available_lots", df.columns)
        self.assertEqual(df.shape[0], 2)

    def test_merge_datasets(self):
        """Test merging static and real-time data"""
        realtime_df = CarparkDataProcessor.format_realtime_data(self.realtime_data)
        merged_df = CarparkDataProcessor.merge_datasets(self.static_data, realtime_df)

        self.assertIn("total_lots", merged_df.columns)
        self.assertEqual(merged_df.loc[merged_df["carpark_number"] == "A1", "available_lots"].values[0], 50)

    def test_handle_missing_values(self):
        """Test handling missing real-time data"""
        realtime_df = pd.DataFrame([])  # Empty DataFrame to simulate missing data
        merged_df = CarparkDataProcessor.merge_datasets(self.static_data, realtime_df)

        self.assertEqual(merged_df.loc[merged_df["carpark_number"] == "A1", "total_lots"].values[0], "N/A")

if __name__ == "__main__":
    unittest.main()
