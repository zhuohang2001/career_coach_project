import pandas as pd
import json
import requests


class CarparkDataLoader:
    """Handles loading of static (CSV) and real-time (JSON/API) carpark data."""

    @staticmethod
    def load_csv(file_path):
        """Loads the static carpark dataset from a CSV file with error handling."""
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: CSV file '{file_path}' not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: CSV file '{file_path}' is empty.")
        except Exception as e:
            print(f"Unexpected Error while loading CSV: {e}")
        return None

    @staticmethod
    def load_json(json_path=None, api_url=None):
        """
        Fetches real-time car park availability data from the provided API.

        - Sends a GET request to the API.
        - Extracts only the latest available `carpark_data` entry.
        - If the request fails, returns None.

        Args:
            api_url (str): API endpoint URL.

        Returns:
            list[dict] | None: JSON list of car park data, or None if the request fails.
        """
        try:
            if api_url:
                response = requests.get(api_url, timeout=10)
                response.raise_for_status()  # Raise an error if API call fails
                return response.json().get("items", [{}])[0].get("carpark_data", [])

            elif json_path:
                with open(json_path, "r") as file:
                    return json.load(file).get("items", [{}])[0].get("carpark_data", [])

        except requests.exceptions.Timeout:
            print(f"API Timeout: Failed to fetch data from {api_url}")
        except requests.exceptions.ConnectionError:
            print(f"Network Error: Unable to connect to {api_url}")
        except requests.exceptions.RequestException as e:
            print(f"API Request Error: {e}")  # Catch all API-related errors
        except json.JSONDecodeError:
            print(f"Error: JSON file '{json_path}' is not formatted correctly.")
        except FileNotFoundError:
            print(f"Error: JSON file '{json_path}' not found.")
        except Exception as e:
            print(f"Unexpected Error: {e}")  # Catch-all for unexpected issues

        return []  # Always return an empty list to prevent crashes
