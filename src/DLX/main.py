import os
import yaml
from messaging import send_messages
from rescuer import rescue_lost_messages

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.yaml")

    # print("Current working directory: {}".format(config_path))
    # print("Config file path: {}".format(config_path))

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    send_messages(config)

    user_input = input("Do you want to rescue the lost messages? (y/n): ")

    if user_input.lower() == "y":
        rescue_lost_messages(config)

if __name__ == "__main__":
    main()