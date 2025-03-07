import unittest
import pandas as pd
from src.cli_handler import CarparkCLI
from io import StringIO
import sys

class TestCarparkCLI(unittest.TestCase):

    def setUp(self):
        """Create sample carpark data for testing"""
        self.merged_data = pd.DataFrame({
            "carpark_number": ["A1", "B2"],
            "address": ["Blk 123", "Blk 456"],
            "total_lots": [100, 200],
            "available_lots": [50, 150],
            "last_updated": ["2025-03-07T17:06:52", "2025-03-07T17:06:52"]
        })

    def capture_output(self, func, *args):
        """Captures stdout output of a function"""
        output = StringIO()
        sys.stdout = output
        func(*args)
        sys.stdout = sys.__stdout__
        return output.getvalue()

    def test_search_by_carpark_valid(self):
        """Test search by valid carpark number"""
        output = self.capture_output(CarparkCLI.search_by_carpark, self.merged_data, "A1")
        self.assertIn("Blk 123", output)

    def test_search_by_carpark_invalid(self):
        """Test search for non-existent carpark number"""
        output = self.capture_output(CarparkCLI.search_by_carpark, self.merged_data, "Z99")
        self.assertIn("No carpark found for the given number.", output)

    def test_search_by_address_valid(self):
        """Test search by valid address keyword"""
        output = self.capture_output(CarparkCLI.search_by_address, self.merged_data, "Blk 123")
        self.assertIn("Blk 123", output)

    def test_search_by_address_invalid(self):
        """Test search for non-existent address"""
        output = self.capture_output(CarparkCLI.search_by_address, self.merged_data, "Random Place")
        self.assertIn("No matching carparks found.", output)

if __name__ == "__main__":
    unittest.main()
