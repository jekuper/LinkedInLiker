import json
import os

class Configuration:
    def __init__(self, config_path):
        # Define attributes with default values for IntelliSense support
        self.config_path: str = config_path
        self.llm_path: str = None
        self.username: str = None
        self.password: str = None
        self.manual: bool = None
        self.post_count: int = 1

        # Load and apply configuration
        self.load_config()

    def load_config(self):
        if not self.config_path.endswith('.json'):
            raise ValueError("The configuration file must be a JSON file.")

        if not os.path.isfile(self.config_path):
            raise FileNotFoundError(f"The file {self.config_path} does not exist.")

        with open(self.config_path, 'r') as file:
            try:
                config_data = json.load(file)
            except json.JSONDecodeError:
                raise ValueError("The configuration file does not contain valid JSON.")

        self.validate_config(config_data)
        self.apply_config(config_data)

    def validate_config(self, config_data):
        required_fields = ["llm_path", "username", "password", "manual"]
        for field in required_fields:
            if field not in config_data:
                raise ValueError(f"The configuration file is missing the required field: {field}")

        if not isinstance(config_data["llm_path"], str):
            raise ValueError("The 'llm_path' field must be a string.")

        if not isinstance(config_data["username"], str):
            raise ValueError("The 'username' field must be a string.")

        if not isinstance(config_data["password"], str):
            raise ValueError("The 'password' field must be a string.")

        if not isinstance(config_data["manual"], bool):
            raise ValueError("The 'manual' field must be a boolean.")

        if not isinstance(config_data["post_count"], int):
            raise ValueError("The 'post_count' field must be an int.")

        if not os.path.exists(config_data["llm_path"]):
            raise FileNotFoundError(f"The path specified in 'llm_path' does not exist: {config_data['llm_path']}")

    def apply_config(self, config_data):
        # Explicitly assign values to attributes
        self.llm_path = config_data["llm_path"]
        self.username = config_data["username"]
        self.password = config_data["password"]
        self.manual = config_data["manual"]
        self.post_count = config_data["post_count"]

# Example usage:
# config = Configuration('path/to/config.json')
# print(config.llm_path)
# print(config.username)
