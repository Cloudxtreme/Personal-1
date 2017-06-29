import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIPY_CLIENT_ID='70be013bbce941b19cc1b0c22d66c6c3'
SPOTIPY_CLIENT_SECRET='7e4bfe34feb942cc8e1f92d7c1293e18'
SPOTIPY_REDIRECT_URI='http://sevone.elchert.net'

token = 'BQARxATcMrHE97GsbiExjR9iXTaVTDahUp3znDarYlhuub6SNIS0dXSkzDglBBdm9Symg1SFwTDu98ykdrH1asxzAsQFAyekvqvlOXMPLDQ36WzLTyPiWIuAH1GwMIA3N-3HZn5_QoLJ1n6482S3'

sp = spotipy.Spotify(auth=token)
print("Current User Info: ")
pprint.pprint(sp.current_user())
print("\n")
print("Current User Playlists: ")
user_playlist = sp.current_user_playlists(limit=5)

for names in user_playlist['items']:
    print names['name']
