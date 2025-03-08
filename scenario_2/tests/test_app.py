from unittest.mock import patch
import unittest
from app import app

class TestCarparkAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test client before running tests."""
        app.testing = True
        cls.client = app.test_client()

    def test_home(self):
        """Test the home endpoint."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Carpark Availability API is running!"})

    def test_get_availability_valid(self):
        """Test fetching carpark availability with a valid carpark ID."""
        response = self.client.get("/get-availability?carpark_id=A12") 
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json().get("result"), list)

    def test_get_availability_invalid(self):
        """Test fetching carpark availability with an invalid carpark ID."""
        response = self.client.get("/get-availability?carpark_id=INVALID123")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Car park not found"})

    def test_get_availability_missing_param(self):
        """Test API without carpark_id parameter (should return 400 Bad Request)."""
        response = self.client.get("/get-availability")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"error": "Missing carpark_id"})

    def test_get_availability_by_address_valid(self):
        """Test searching carparks by valid address keyword."""
        response = self.client.get("/get-availability/search?address=Tampines")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json().get("result"), list)

    def test_get_availability_by_address_invalid(self):
        """Test searching carparks with an address that doesn't exist."""
        response = self.client.get("/get-availability/search?address=INVALID_ADDRESS")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "No matching carparks found"})

    def test_get_availability_by_address_missing_param(self):
        """Test API without an address parameter (should return 400 Bad Request)."""
        response = self.client.get("/get-availability/search")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {"error": "Missing address parameter"})

    @patch("app.merged_data", None)  # This ensures `merged_data` is set to None for this test
    def test_internal_server_error(self):
        """Simulate a scenario where data is not available."""
        response = self.client.get("/get-availability?carpark_id=A1")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {"error": "Data not available"})

if __name__ == "__main__":
    unittest.main()
