import yaml
from messaging import send_messages
from rescuer import rescue_lost_messages

# Step 1: Read values from YAML config
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Step 2: Send messages
send_messages(config)

# Step 3: Ask the user if they want to rescue the lost messages
user_input = input("Do you want to rescue the lost messages? (yes/no): ")

if user_input.lower() == "yes":
    rescue_lost_messages()

