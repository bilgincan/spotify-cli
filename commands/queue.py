from commands.play import search, get_device_id, prepare_authorization_header, get_current_song
from requester import post_request, get_request

def next():
    print("skipping next song...")
    url = "https://api.spotify.com/v1/me/player/next"
    headers = prepare_authorization_header()

    response = post_request(url, headers, None)
    print(response)
    
    get_current_song()
    pass

def previous():
    print("skipping previous song...")
    url = "https://api.spotify.com/v1/me/player/previous"
    headers = prepare_authorization_header()

    response = post_request(url, headers, None)
    print(response)

    get_current_song()
    pass    

def add_item(item):
    print("addItem works " + item)
    device_id = get_device_id()
    spotify_uri = search(item, "track")

    url = "https://api.spotify.com/v1/me/player/queue?uri=" + spotify_uri + "&device_id=" + device_id
    headers = prepare_authorization_header()
    headers["Content-Type"] = "application/json"

    response = post_request(url, headers, None)
    print(response)
    queue = get_queue()
    item = queue[0]

    print("The song added to queue:" + item["artists"][0]["name"] + " - " + item["name"] + "\n")

    pass

def get_queue():
    url = "https://api.spotify.com/v1/me/player/queue"
    headers = prepare_authorization_header()

    response = get_request(url, headers)
    queue = response["queue"]

    return queue

def show_queue():
    queue = get_queue()

    for item in queue:
        print(item["artists"][0]["name"] + " - " + item["name"] + "\n")
