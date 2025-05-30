import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
CLIENT_ID = '1c43d600e51744ffb443fbad427076a2'
CLIENT_SECRET = 'fb9ca19e0db54224baf2bcbdc2ae45c3'
REDIRECT_URI = 'http://example.com'
USERNAME = '317yfnj4xcgsk6yljfwfr4pm37ly'
ID = 'BQDHYzBCwZSVS4ZKhv5COqoggDa7IWevOLfeFR5iJDtuMLnYOSyuo9Htax5ibJ182fYlgCHwpjJOSEjVbaAMv3rr47E2Lo7asrVnfgmXtSQaI1b1LbPcoP32dYokStEnSQTy2jbPgmHVVhANd2qGdlDcP-UBab9G7YIBR3eyw-sTvC-dQQKydTsgvUwzhX_lq04we'
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    cache_path= 'token.txt',
    username= USERNAME,
    show_dialog= True,
    scope= "playlist-modify-private"))
user_id = sp.current_user()["id"]












headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}




response = requests.get("https://www.billboard.com/charts/hot-100/" + date, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
songs=soup.select('li ul li h3')
song_list = [songs.getText().strip() for songs in songs]
print(song_list)

song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user= user_id, name = f'Billboard{date}', public= False,)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
