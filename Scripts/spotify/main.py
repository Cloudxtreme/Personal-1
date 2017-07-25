from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import pprint
import logging
import sqlite3

# https://developer.spotify.com/web-api/get-playlists-tracks/

########################################################################
# create logger
logger = logging.getLogger(__name__)
log = logging.FileHandler('doucheSpotifyUpdate.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log.setLevel(logging.DEBUG)
log.setFormatter(formatter)
logger.addHandler(log)
########################################################################

SPOTIPY_CLIENT_ID='70be013bbce941b19cc1b0c22d66c6c3'
SPOTIPY_CLIENT_SECRET='7e4bfe34feb942cc8e1f92d7c1293e18'
SPOTIPY_REDIRECT_URI='http://sevone.elchert.net'

dbName = "playlist"

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:nonstopflights:playlist:4w6pMMEL61mOFQIeIjL9uy'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

resultsObject = sp.user_playlist(username, playlist_id)
logger.debug('Retrieve resultsObject: %s', resultsObject)

def createTables():
    """ Make sure table is created in databse file """

    try:
        if conn is not None:
            c.execute('''CREATE TABLE if not exists playlist(
                         addedBy TEXT,
                         addedAt TEXT,
                         url TEXT,
                         artistName TEXT,
                         trackName TEXT,
                         spotifyId TEXT
                         )''')
            logger.info("Created new database tables.")

    except (RuntimeError, TypeError, NameError) as e:
        print(e)
        logger.error('Error creating database/tables')

def insertTrack(addedBy, addedAt, url, artistName, trackName, spotifyId):
    """ Insert into sqllite """
    t = (addedBy, addedBy, url, artistName, trackName, spotifyId)
    try:
        if conn is not None:
            c.execute('INSERT INTO playlist VALUES (?, ?, ?, ?, ?, ?)', t)
    except:
        print(Exception)
        logger.error('Exception: %s', Exception)
    finally:
        conn.commit()

###########################################################################
''' Connect to Database '''
conn = sqlite3.connect(dbName)
c = conn.cursor()
logger.debug('-- Logging into Database')
###########################################################################
''' Create database if not there '''
createTables()
logger.debug("Check for Database")
###########################################################################

def firstSync():
    '''
    Download all information for the first time Created
    and insert to database
    '''
    for track in resultsObject['tracks']['items']:
        addedBy = track['added_by']['id']
        addedAt = track['added_at']
        url = track['track']['artists'][0]['external_urls']['spotify']
        artistName = track['track']['artists'][0]['name']
        trackName = track['track']['name']
        spotifyId = track['track']['id']

        insertTrack(addedBy, addedAt, url, artistName, trackName, spotifyId)
        pprint.pprint(track)
        logger.debug("addedBy: %s addedAt: %s artistName: %s trackName: %s\n URL: %s", addedBy, addedAt, artistName, trackName, url)

firstSync()
