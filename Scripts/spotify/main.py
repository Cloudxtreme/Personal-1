from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import os
import logging
import sqlite3

# https://developer.spotify.com/web-api/get-playlists-tracks/

########################################################################
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log = logging.FileHandler('spotify.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log.setFormatter(formatter)
logger.addHandler(log)
########################################################################

SPOTIPY_CLIENT_ID='70be013bbce941b19cc1b0c22d66c6c3'
SPOTIPY_CLIENT_SECRET='7e4bfe34feb942cc8e1f92d7c1293e18'
SPOTIPY_REDIRECT_URI='http://sevone.elchert.net'



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
            logger.info("Tried to create new database tables.")
            conn.commit()

    except (RuntimeError, TypeError, NameError) as e:
        print(e)
        logger.error('Error creating database/tables')

def insertTrack(addedBy, addedAt, url, artistName, trackName, spotifyId):
    """ Insert into sqllite """
    t = (addedBy, addedAt, url, artistName, trackName, spotifyId, 0)
    logger.info("InsertTrack: %s", t)
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
    ''' This will display the json for the playlist '''
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
        logger.debug("Pulled info. addedBy - %s, addedAt - %s, artistName - %s, trackname -%s", addedBy, addedAt, artistName, trackName)

        # check if track exists in database
        queryId = c.execute('select spotifyId from playlist where spotifyId=(?);', [spotifyId])
        data = queryId.fetchone()
        logger.debug('Query spotifyId to see if it exists - %s', queryId.fetchone())
        if data is None:
            logger.info('Track not found in database - %s - %s', artistName, trackName)
            insertTrack(addedBy, addedAt, url, artistName, trackName, spotifyId)
            logger.debug('Inserting Track: %s', spotifyId)
            print('Inserted Data: {}'.format(spotifyId))
            conn.commit()

###########################################################################

def getMostRecentRon():
    ''' query database for most recently added song'''
    ronDatabaseObject = c.execute('select * from playlist where addedBy="ronlipke" order by addedAt desc limit 1')
    ronDatabaseList = ronDatabaseObject.fetchone()
    logger.info('Most Recent Ron track: %s', ronDatabaseList)
    return ronDatabaseList

def getMostRecentAdam():
        ''' query database for most recently added song'''
        adamDatabaseObject = c.execute('select * from playlist where addedBy="nonstopflights" order by addedAt desc limit 1')
        adamDatabaseList = adamDatabaseObject.fetchone()
        logger.info('Most Recent Adam Track: %s', adamDatabaseList)
        return adamDatabaseList

###########################################################################
''' Connect to Database '''
try:
    dbName = "playlist"
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    logger.info('Connecting to database')
except:
    logger.error("Error: %s", Exception)
###########################################################################
''' Create database if not there '''
createTables()
logger.info('Running createTables()')
###########################################################################
''' Pulls new tracks from playlist and inserts to database, if needed '''
syncAndInsert()
logger.info('Running Sync and Insert')

# get list of most recent track info
# example:
# ('ronlipke', '2017-07-15T17:19:35Z',
#'https://open.spotify.com/artist/6ITIhwzOeoG3BjX3Es1q0T', 'Celebration',
#'Rolling On', '4IrWkDddyMrPYYQdH7jozX', 0)

ronMostRecentTrackList = getMostRecentRon()

if ronMostRecentTrackList[6] == 0:
    print("New Ronald Track")
    print(ronMostRecentTrackList[6])
    spotId = ronMostRecentTrackList[5]
    c.execute('update playlist set newest=0 where addedBy="ronlipke";')
    c.execute('update playlist set newest=1 where spotifyId=(?)', [spotId])
    os.system('mail -s "New Ron Track" adam@elchert.net')
    conn.commit()
else:
    print('No New Ron Track')
    logger.info("No New Ron Tracks")

adamMostRecentTrackList = getMostRecentAdam()

if adamMostRecentTrackList[6] == 0:
    print("New Adam Track")
    spotId = adamMostRecentTrackList[5]
    c.execute('update playlist set newest=0 where addedBy="nonstopflights";')
    c.execute('update playlist set newest=1 where spotifyId=(?)', [spotId])
    os.system('mail -s "New Adam Track" adam@elchert.net')

    conn.commit()
else:
    print('No New Adam Track')
    logger.info("No New Adam Tracks")




# set newest track to 1 in db
# ronObject = getMostRecentRon()
# ronTrack = ronObject[5]
# c.execute('update playlist set newest=1 where spotifyId=(?)', [ronTrack])
# print('Updated Ron newest with spot id: {}'.format(ronTrack))
#
# adamObject = getMostRecentAdam()
# adamTrack = adamObject[5]
# c.execute('update playlist set newest=1 where spotifyId=(?)', [adamTrack])
# print('Updated Adam newest with spot id: {}'.format(adamTrack))
# conn.commit()

#print(debug__pullJson(resultsObject))
#print(getMostRecentRon())
conn.close()
# # ----> pull json
# # ----> sort by date, user -> get spotifyId
# # ----> write newest to json file
