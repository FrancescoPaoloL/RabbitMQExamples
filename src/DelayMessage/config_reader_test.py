import os
import unittest
import yaml
from config_reader import read_config

class TestReadConfig(unittest.TestCase):
    def setUp(self):
        # Create temporary YAML files with different configurations
        self.config_data = {
            "messages_count": 500,
            "start_datetime": "2023-01-01 12:00:00",
            "probability": 30000,
            "delayed_exchange": "custom_exchange",
            "queue": "custom_queue"
        }

        self.temp_yaml_file = "~config_test.yaml"
        with open(self.temp_yaml_file, "w") as f:
            yaml.dump(self.config_data, f)

    def tearDown(self):
        # Remove temporary YAML file after each test
        os.remove(self.temp_yaml_file)

    def test_read_config_with_valid_data(self):
        delay_ms, start_datetime, expiration_ms, delayed_exchange, delayed_queue = read_config(self.temp_yaml_file)
        self.assertEqual(delay_ms, self.config_data["messages_count"])
        self.assertEqual(start_datetime, self.config_data["start_datetime"])
        self.assertEqual(expiration_ms, self.config_data["probability"])
        self.assertEqual(delayed_exchange, self.config_data["delayed_exchange"])
        self.assertEqual(delayed_queue, self.config_data["queue"])

    def test_read_config_with_missing_properties(self):
        missing_properties_config = {
            "start_datetime": "2023-01-01 12:00:00",
            "delayed_exchange": "custom_exchange"
        }
        with open(self.temp_yaml_file, "w") as f:
            yaml.dump(missing_properties_config, f)

        delay_ms, start_datetime, expiration_ms, delayed_exchange, delayed_queue = read_config(self.temp_yaml_file)
        self.assertEqual(delay_ms, 5000)  # Default value
        self.assertEqual(start_datetime, missing_properties_config["start_datetime"])
        self.assertEqual(expiration_ms, 20000)  # Default value
        self.assertEqual(delayed_exchange, missing_properties_config["delayed_exchange"])
        self.assertEqual(delayed_queue, "delayed_queue")  # Default value

if __name__ == '__main__':
    unittest.main()
