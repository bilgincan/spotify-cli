import requests

def get_request(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)

def post_request(url, headers, body):
    try:
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)

def put_request(url, headers, body):
    try:
        response = requests.put(url, headers=headers, data=body)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        print(err)
        print(err.response.text)
        exit(1)
