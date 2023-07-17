import json

def save_json_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def get_access_token():
    with open("token.json") as file:
        data = json.load(file)
        return data["access_token"]