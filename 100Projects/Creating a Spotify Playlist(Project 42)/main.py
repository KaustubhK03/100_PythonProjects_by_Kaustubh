from dotenv import load_dotenv
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
USER_ID = os.getenv("USER_ID")
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=BILLBOARD_URL)
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")
lst_of_h3s = soup.select(selector="li ul li h3")
song_lst = [song.get_text().replace("\n", "").replace("\t", "") for song in lst_of_h3s]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USER_ID,
    )
)
user_id = sp.current_user()["id"]

uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in song_lst]

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID, public=False, name=f"{date} BillBoard-100")['id']
sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=uris)
