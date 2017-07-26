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
log.setLevel(logging.WARNING)
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
                         spotifyId TEXT,
                         newest INTEGER DEFAULT 0
                         )''')
            logger.info("Created new database tables.")

    except (RuntimeError, TypeError, NameError) as e:
        print(e)
        logger.error('Error creating database/tables')

def insertTrack(addedBy, addedAt, url, artistName, trackName, spotifyId):
    """ Insert into sqllite """
    t = (addedBy, addedAt, url, artistName, trackName, spotifyId, 0)
    try:
        if conn is not None:
            c.execute('INSERT INTO playlist VALUES (?, ?, ?, ?, ?, ?, ?)', t)
            logger.debug('Inserted ID: {}'.format(spotifyId))
    except:
        print(Exception)
        logger.error('Exception: %s', Exception)
    finally:
        conn.commit()

def debug__pullJson(resultsObject):
    #pprint.pprint(resultsObject)
    for track in resultsObject['tracks']['items']:

        addedBy = track['added_by']['id']
        addedAt = track['added_at']
        url = track['track']['artists'][0]['external_urls']['spotify']
        artistName = track['track']['artists'][0]['name']
        trackName = track['track']['name']
        spotifyId = track['track']['id']

        print("Added By: {}".format(addedBy))
        print("Added At: {}".format(addedAt))
        print("Url: {}".format(url))
        print('ArtistName: {}'.format(artistName))
        print('trackName: {}'.format(trackName))
        print('SpotifyId: {}'.format(spotifyId))
        print('\n')



def syncAndInsert():
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

        # check if track exists in database
        queryIdFromDatabase = c.execute('select spotifyId from playlist where spotifyId=(?);', [spotifyId])

        # if it doesn't, insert it
        if queryIdFromDatabase is None:
            #print(queryIdFromDatabase.fetchone()[0])
            insertTrack(addedBy, addedAt, url, artistName, trackName, spotifyId, 0)
            logger.info('Inserted Track - Artist: {} - trackname: {}'.format(artistName, trackName))

###########################################################################

def getMostRecentRon():
    ''' query database for most recently added song'''
    ronDatabaseObject = c.execute('select * from playlist where addedBy="ronlipke" order by addedAt desc limit 1')
    ronDatabaseList = ronDatabaseObject.fetchone()
    return ronDatabaseList

def getMostRecentAdam():
        ''' query database for most recently added song'''
        adam = c.execute('select * from playlist where addedBy="nonstopflights" order by addedAt desc limit 1')
        adamDatabaseList = adamDatabaseObject.fetchone()
        return adamDatabaseList

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

#debug__pullJson(resultsObject)
syncAndInsert()
#getMostRecentRon()

conn.close()
# ----> pull json
# ----> sort by date, user -> get spotifyId
# ----> write newest to json file
