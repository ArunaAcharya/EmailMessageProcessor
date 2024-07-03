import os 
import json

folder_path = os.path.dirname(__file__) 
file_path = os.path.join(folder_path,'..', 'config.json')


with open (file_path, 'r') as file:
    config_json = json.load(file)


def get_config():
    with open (file_path, 'r') as file:
        config_json = json.load(file)
    return config_json
