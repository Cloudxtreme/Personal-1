from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import pprint

SPOTIPY_CLIENT_ID='70be013bbce941b19cc1b0c22d66c6c3'
SPOTIPY_CLIENT_SECRET='7e4bfe34feb942cc8e1f92d7c1293e18'
SPOTIPY_REDIRECT_URI='http://sevone.elchert.net'

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:nonstopflights:playlist:4w6pMMEL61mOFQIeIjL9uy'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

times = []

resultsObject = sp.user_playlist(username, playlist_id)
try:
    for track in resultsObject['tracks']['items']:
        artistName = track['track']['artists'][0]['name']
        trackName = track['track']['name']
        url = track['track']['artists'][0]['external_urls']['spotify']
        addedBy = track['added_by']['id']
        addedAt = track['added_at']
        print("addedBy: {}\n addedAt: {}\n artistName: {}\n trackName: {}\n URL: {}\n".format(addedBy, addedAt, artistName, trackName, url))
        times.append(addedAt)
except UnicodeError:
    pass
print("times: \n")
print(times)
print("Max Times: \n")
print(max(times))
