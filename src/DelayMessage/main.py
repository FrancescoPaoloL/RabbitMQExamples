from config_reader import read_config
from datetime import datetime
from message_publisher import publish_with_delay
from datetime_calculator import calculate_delay_until_next_datetime

def main():
    delay_ms, start_datetime, expiration_ms, delayed_exchange, delayed_queue = read_config("config.yaml")

    # Delay in milliseconds
    message = "Hello, RabbitMQ! (Delayed by {} ms)".format(delay_ms)
    publish_with_delay(message, delay_ms, expiration_ms, delayed_exchange, delayed_queue)

    # Delay as datetime
    message = "Hello, RabbitMQ! (Delayed by datetime)"
    start_datetime_formatted = datetime.strptime(str(start_datetime), '%Y-%m-%d %H:%M:%S')
    delay_dt = (calculate_delay_until_next_datetime(start_datetime_formatted) - datetime.now()).total_seconds() * 1000

    if delay_dt > 0:
        publish_with_delay(message, delay_dt, expiration_ms, delayed_exchange, delayed_queue)
    else:
        print("The specified datetime is in the past. No message will be published.")

if __name__ == "__main__":
    main()
