import json
import csv

def json_to_csv(json_filename, csv_filename):
    """Converts a JSON array to a CSV file."""
    try:
        with open(json_filename, 'r') as json_file:
            data = json.load(json_file)

        if not data:
            print("JSON file is empty.")
            return

        # Extract keys for CSV header
        keys = data[0].keys()

        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"JSON data successfully converted to {csv_filename}")

    except FileNotFoundError:
        print("JSON file not found.")

    except json.JSONDecodeError:
        print("Error decoding JSON file.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    json_filename = "data.json"   # Replace with your JSON file name
    csv_filename = "output.csv"   # Output CSV file
    json_to_csv(json_filename, csv_filename)
