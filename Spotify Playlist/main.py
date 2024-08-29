from bs4 import BeautifulSoup
import requests, os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


print("I want a year around which you want a spotify playlist of top 100 songs")
year = input("Provide me the year (ex: 2002): ")
month = input("Provide me the month (ex: 02): ")
day = input("Provide me the day (ex: 25): ")
date = year + "-" + month + "-" + day


response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
song_names = soup.select(selector = "li h3")
song_names_only = [song.get_text().strip() for song in song_names if "\n" not in song]
print(song_names_only)

spot = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = "playlist-modify-private",
                                                   client_id = os.getenv("client_id"),
                                                   client_secret= os.getenv("client_secret"),
                                                   redirect_uri = "http://example.com",
                                                   show_dialog = True,
                                                   cache_path = "token.txt"))

user = spot.current_user()
user_id = user["id"]
song_uri_list = []

for single_song in song_names_only:
    found = spot.search(q = f"track:{single_song}", type="track", limit = 1)
    try:
        uri = found["tracks"]["items"][0]["uri"]
    except IndexError:
        pass
    else:
        song_uri_list.append(uri)

create_playlist = spot.user_playlist_create(user = user_id, name = f"Top 100 songs of {year}", public = False)
spot.playlist_add_items(playlist_id = create_playlist["id"], items = song_uri_list, position = 0)



