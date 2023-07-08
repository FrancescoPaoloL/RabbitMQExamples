from config_reader import read_config
from messaging import send_messages
from rescuer import rescue_lost_messages

def main():
    host, messages_count, probability, ex_dlx, queue, queue_dlx, TTL = read_config("config.yaml")
    send_messages(messages_count, probability, ex_dlx, queue, queue_dlx, TTL)

    user_input = input("Do you want to rescue the lost messages? (y/n): ")

    if user_input.lower() == "y":
        rescue_lost_messages(host, queue, queue_dlx)

if __name__ == "__main__":
    main()