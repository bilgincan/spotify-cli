import os
from requester import post_request
import dotenv
from utils_file import save_json_to_file

dotenv.load_dotenv()

client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
client_id = os.getenv("SPOTIFY_CLIENT_ID")

def login():
    os.system("cd web-auth")
    os.system("cd web-auth/spotify-profile-demo")
    os.system("npm install")
    os.system("ls")
    print("go to localhost:5173")
    os.system("npm run dev")


    

def logout():
    print("logout works")
    pass