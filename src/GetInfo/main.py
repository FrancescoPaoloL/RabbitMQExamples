from config_reader import read_config
import requests
from tabulate import tabulate

# Basic authentication credentials
username = "guest"
password = "guest"

def fetch_data(endpoint):
    response = requests.get(endpoint, auth=(username, password))
    return response.json()

def print_section(title, data, fields):
    formatted_data = []
    for item in data:
        row = [item.get(field, "") for field in fields]
        if any(row):
            formatted_data.append(row)

    if formatted_data:
        print(title + ":")
        print(tabulate(formatted_data, headers=fields, tablefmt="grid"))
        print()
    else:
        print(f"{title} is empty.")
        print()

def main():
    api_url = read_config("config.yaml")

    # Fetch overall RabbitMQ overview
    overview_data = fetch_data(f"{api_url}/overview")
    overview_fields = ["node", "messages", "consumers", "queues"]
    print_section("RabbitMQ Overview", [overview_data], overview_fields)

    # Fetch list of queues
    queues_data = fetch_data(f"{api_url}/queues/%2f")
    queues_fields = ["name", "messages", "consumers"]
    print_section("List of Queues", queues_data, queues_fields)

    # Fetch list of exchanges
    exchanges_data = fetch_data(f"{api_url}/exchanges/%2f")
    exchanges_fields = ["name", "type"]
    print_section("List of Exchanges", exchanges_data, exchanges_fields)

if __name__ == "__main__":
    main()
