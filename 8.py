import requests

num_records_processed = 0

def get_json_data(url):
    response = requests.get(url)
    return response.json()

def process_data(json_data):
    processed_data = []
    for item in json_data:
        processed_data.append(item['name'])

    return processed_data

def update_processed_records(data):
    global num_records_processed
    num_records_processed += len(data)

def main():
    url = 'https://jsonplaceholder.typicode.com/users'

    json_data = get_json_data(url)

    processed_data = process_data(json_data)

    update_processed_records(processed_data)

    print("Number of records processed:", num_records_processed)

main()
