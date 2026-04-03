import csv

def count_rows(csv_filename):
    try:
        with open(csv_filename, "r", newline="") as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)
            print(f"Total number of rows: {row_count}")
    
    except FileNotFoundError:
        print("File not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    filename = "data.csv"   # <-- put your CSV file name here
    count_rows(filename)
