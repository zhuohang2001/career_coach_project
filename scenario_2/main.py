from src.load_data import CarparkDataLoader
from src.process_data import CarparkDataProcessor
from src.cli_handler import CarparkCLI
import argparse

# File paths
CSV_FILE = "data/HDBCarparkInformation.csv"
JSON_FILE = "data/carpark-availability.json"
API_URL = "https://api.data.gov.sg/v1/transport/carpark-availability"  # If using API

def main():
    """Loads, processes, and runs the carpark availability CLI application."""

    # Load datasets
    static_data = CarparkDataLoader.load_csv(CSV_FILE)
    realtime_data = CarparkDataLoader.load_json(api_url=API_URL)

    if static_data is None or realtime_data is None:
        print("Data Load Failed. Exiting...")
        return

    # Process data
    realtime_df = CarparkDataProcessor.format_realtime_data(realtime_data)
    merged_data = CarparkDataProcessor.merge_datasets(static_data, realtime_df)

    # CLI Arguments
    parser = argparse.ArgumentParser(description="Carpark Availability CLI")
    parser.add_argument("--carpark", type=str, help="Find details by carpark number")
    parser.add_argument("--address", type=str, help="Search by address keyword")
    args = parser.parse_args()

    if args.carpark:
        CarparkCLI.search_by_carpark(merged_data, args.carpark)
    elif args.address:
        CarparkCLI.search_by_address(merged_data, args.address)
    else:
        print("Info: Use --carpark <number> or --address <keyword> to search.")

if __name__ == "__main__":
    main()
