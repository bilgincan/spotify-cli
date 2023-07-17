from utils_file import get_access_token
from requester import get_request, put_request
import json

access_token = get_access_token()

def prepare_authorization_header():
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
     
    return headers

def get_playback_state():
    url = "https://api.spotify.com/v1/me/player"
    headers = prepare_authorization_header()

    response = get_request(url, headers)
    return response

def get_device_id():
    playback_state = get_playback_state()
    device_id = playback_state["device"]["id"]
    return device_id

def search(song, type):
    url = "https://api.spotify.com/v1/search?type={}&".format(type) + f"q={song}&limit=1"
    headers = prepare_authorization_header()

    response = get_request(url, headers)

    return response["tracks"]["items"][0]["uri"]


def pause():
    print("pausing...")
    device_id = get_device_id()

    url = "https://api.spotify.com/v1/me/player/pause"
    headers = prepare_authorization_header()
    headers["Content-Type"] = "application/json"

    body = {
        "device_id": device_id
    }

    body = json.dumps(body)

    response = put_request(url, headers, body)
    print(response)
    pass

def resume():
    print("playing current song...")
    device_id = get_device_id()

    url = "https://api.spotify.com/v1/me/player/play"
    headers = prepare_authorization_header()
    headers["Content-Type"] = "application/json"

    body = {
        "device_id": device_id
    }

    body = json.dumps(body)

    response = put_request(url, headers, body)
    pass

def play(song):
    print("play works with the song: " + song)
    device_id = get_device_id()

    url = "https://api.spotify.com/v1/me/player/play"
    headers = prepare_authorization_header()
    headers["Content-Type"] = "application/json"
    song_uri = search(song, "track")

    body = {
        "uris": [song_uri],
        "position_ms": 0,
        "device_id": device_id
    }

    body = json.dumps(body)

    response = put_request(url, headers, body)
    print(response)
    pass

def play_playlist(playlist):
    print("play_playlist works with the playlist: " + playlist)
    pass

# bonus
def play_genre(genre):
    print("play_genre works with the genre: " + genre)
    pass

def get_current_song():
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = prepare_authorization_header()

    response = get_request(url, headers)
    print(response["item"]["album"]["artists"][0]["name"] + " - " + response["item"]["name"])
    print("Link: " + response["item"]["external_urls"]["spotify"])
    pass

def shuffle():
    print("shuffle works")
    pass