import requests

# Global variable to store the number of records processed
num_records_processed = 0

def get_json_data(url):
    response = requests.get(url)
    return response.json()

def process_data(json_data):
    # Local variables to store intermediate values
    processed_data = []

    # Process the relevant data from the JSON response
    for item in json_data:
        processed_data.append(item['name'])

    return processed_data

def update_processed_records(data):
    # Access the global variable using the global keyword
    global num_records_processed
    num_records_processed += len(data)

def main():
    # URL for the API
    url = 'https://jsonplaceholder.typicode.com/users'

    # Step 1: Retrieve JSON data from the API
    json_data = get_json_data(url)

    # Step 2: Process the relevant data using local variables
    processed_data = process_data(json_data)

    # Step 3: Update the number of processed records using global variable
    update_processed_records(processed_data)

    # Print the number of records processed
    print("Number of records processed:", num_records_processed)

# Run the main program
main()
