from sender import Message
from sender import Mail
from sender import Attachment
from time import strftime
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log = logging.FileHandler('logs/smtp.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log.setFormatter(formatter)
logger.addHandler(log)

dbName = "tweets.db"

def updateFile():
    '''
    runs database query to pull non-mailed tweets
    '''
    if not os.path.isfile('fileOutput.txt'):
        os.system('touch fileOutput.txt')
        logger.info("fileOutput.txt was created.")

    try:
        command = 'sqlite3 -column tweets.db "select username, tweetText, tweetURL from tweets where mailed=0" > fileOutput.txt'
        output = os.system(command)
        logger.info('Queries database for new tweets')

        try:
            updateCommand = 'sqlite3 tweets.db "update tweets set mailed=1;"'
            updateMailed = os.system(updateCommand)
            logger.info('Set tweets to mailed=1')
        except Exception as e:
            print(e)

        return(output)

    except Exception as e:
        print(e)
        logger.debug('Exception: %s', [e])


# SMTP log in information
mail = Mail("mail.messagingengine.com",
            port=465, username="aschoonover@fastmail.fm",
            password="MkaV3yYevpvKqbT2RarY",
            use_tls=False, use_ssl=True, debug_level=None)

# email message object
msg = Message(fromaddr=("Adam Elchert", "adam@elchert.net"))

updateFile()
logger.info('Running UpdateFile()')

# attachment
with open('fileOutput.txt') as fileOutput:
    attachment = fileOutput.read()

fileOutput.close()

# update message object
msg.fromaddr = ("adam@elchert.net")
msg.body= '{}'.format(attachment)
msg.to = ('adam@elchert.net')
msg.subject=('Tweets from {}'.format(strftime('%B %d')))
mail.send(msg)
logger.info('Sent Email')
logger.debug('Debug: %s', [msg])


os.remove('fileOutput.txt')
