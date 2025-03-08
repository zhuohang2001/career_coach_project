from flask import Flask, request, jsonify
from src.load_data import CarparkDataLoader
from src.process_data import CarparkDataProcessor
from src.cli_handler import CarparkCLI

app = Flask(__name__)

# File paths
CSV_FILE = "data/HDBCarparkInformation.csv"
API_URL = "https://api.data.gov.sg/v1/transport/carpark-availability"

# Load and process data
static_data = CarparkDataLoader.load_csv(CSV_FILE)
realtime_data = CarparkDataLoader.load_json(api_url=API_URL)

if static_data is not None and realtime_data is not None:
    realtime_df = CarparkDataProcessor.format_realtime_data(realtime_data)
    merged_data = CarparkDataProcessor.merge_datasets(static_data, realtime_df)
else:
    merged_data = None

@app.route("/")
def home():
    return jsonify({"message": "Carpark Availability API is running!"})

@app.route("/get-availability", methods=["GET"])
def get_availability():
    """Fetch carpark details by carpark ID."""
    carpark_id = request.args.get("carpark_id")
    if not carpark_id:
        return jsonify({"error": "Missing carpark_id"}), 400

    if merged_data is None:
        return jsonify({"error": "Data not available"}), 500

    result = CarparkCLI.search_by_carpark(merged_data, carpark_id)
    print("res: ", result)
    if not result:
        return jsonify({"error": "Car park not found"}), 404

    return jsonify(result)

@app.route("/get-availability/search", methods=["GET"])
def get_availability_by_address():
    """Search carparks by address keyword."""
    address_keyword = request.args.get("address")
    if not address_keyword:
        return jsonify({"error": "Missing address parameter"}), 400

    if merged_data is None:
        return jsonify({"error": "Data not available"}), 500

    result = CarparkCLI.search_by_address(merged_data, address_keyword)

    if not result:
        return jsonify({"error": "No matching carparks found"}), 404

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
