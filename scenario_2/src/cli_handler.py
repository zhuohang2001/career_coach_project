import pandas as pd


class CarparkCLI:
    """Handles user queries for carpark details."""

    @staticmethod
    def search_by_carpark(merged_df, carpark_number):
        """Fetches and displays details of a carpark by number."""
        result = merged_df[merged_df["carpark_number"] == carpark_number]
        if not result.empty:
            print("\n🔹 Carpark Details:")
            print(result.to_string(index=False))
            last_update = result["last_updated"].values[0] if "last_updated" in result.columns else "Unknown"
            print("\nLast Updated:", last_update)
        else:
            print("No carpark found for the given number.")

    @staticmethod
    def search_by_address(merged_df, keyword):
        """Finds carparks that match an address keyword."""
        filtered_df = merged_df[merged_df["address"].str.contains(keyword, case=False, na=False)]
        if not filtered_df.empty:
            print("\n🔹 Matching Carparks:")
            print(filtered_df.to_string(index=False))
            last_update = filtered_df["last_updated"].values[0] if "last_updated" in filtered_df.columns else "Unknown"
            print("\nLast Updated:", last_update)
        else:
            print("No matching carparks found.")

