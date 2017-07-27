
import json
import sqlite3, pprint

# https://developer.spotify.com/web-api/get-playlists-tracks/
dbName = "playlist"
conn = sqlite3.connect(dbName)
c = conn.cursor()

query = c.execute('select spotifyId from playlist where addedBy="nonstopflights" order by addedAt asc limit 1;')
data = query.fetchone()[0]
print(data)
username = 'nonstopflights'
person = {username: data}


with open('data.txt', 'r') as outfile:
     data = json.load(outfile)

pprint.pprint(data)
