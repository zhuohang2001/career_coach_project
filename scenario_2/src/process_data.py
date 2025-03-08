import pandas as pd

class CarparkDataProcessor:
    """Handles merging and processing of carpark datasets."""

    @staticmethod
    def format_realtime_data(realtime_data):
        """Converts real-time carpark data into a structured DataFrame."""
        df = pd.DataFrame([
            {
                "carpark_number": item.get("carpark_number", "Unknown"),
                "total_lots": item.get("carpark_info", [{}])[0].get("total_lots", "N/A"),
                "available_lots": item.get("carpark_info", [{}])[0].get("lots_available", "N/A"),
                "last_updated": item.get("update_datetime", "N/A")
            }
            for item in realtime_data
        ])

        # Convert numeric columns safely, but keep missing values as "N/A"
        df["total_lots"] = pd.to_numeric(df["total_lots"], errors="coerce")
        df["available_lots"] = pd.to_numeric(df["available_lots"], errors="coerce")

        df.fillna("N/A", inplace=True)  # Ensure missing values are "N/A"

        return df

    @staticmethod
    def merge_datasets(static_df, realtime_df):
        """
        Merges static car park dataset with real-time availability data.

        - Performs a **left join** to ensure that all static car parks are retained.
        - If real-time data is missing, it indicates the car park was not updated in the latest API call.
        - Ensures that `carpark_number` from the API aligns with `car_park_no` from static data.

        Args:
            static_df (pd.DataFrame): Static car park details.
            realtime_df (pd.DataFrame): Real-time availability data.

        Returns:
            pd.DataFrame: Merged dataset containing both static and real-time details.
        """

        # Standardize column names
        static_df.rename(columns={"car_park_no": "carpark_number"}, inplace=True)

        # Handle empty `realtime_df` to prevent merge errors
        if realtime_df.empty or "carpark_number" not in realtime_df.columns:
            print("Warning: Real-time data is empty. Using placeholder values.")
            realtime_df = pd.DataFrame({
                "carpark_number": static_df["carpark_number"],
                "total_lots": "N/A",
                "available_lots": "N/A",
                "last_updated": "Unknown"
            })

        combined_df = static_df.merge(realtime_df, on="carpark_number", how="left")

        # Fill missing values with strings to match test expectations
        fill_values = {
            "address": "Unknown",
            "total_lots": "N/A",  # Ensure it remains a string
            "available_lots": "N/A",
            "last_updated": "Unknown",
            "type_of_parking_system": "Unknown",
            "short_term_parking": "Not Available",
            "free_parking": "Unknown",
            "night_parking": "Unknown",
            "x_coord": "0.0",
            "y_coord": "0.0"
        }
        combined_df.fillna(fill_values, inplace=True)

        return combined_df
