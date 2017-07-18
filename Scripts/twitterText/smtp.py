from sender import Message
from sender import Mail
from sender import Attachment
from time import strftime
import os

dbName = "tweets.db"

def updateFile():
    '''
    runs database query to pull non-mailed tweets
    '''
    try:
        command = 'sqlite3 -column tweets.db "select username, tweetText, tweetURL from tweets where mailed=0" > fileOutput.txt'
        output = os.system(command)

        try:
            updateCommand = 'sqlite3 tweets.db "update tweets set mailed=1;"'
            updateMailed = os.system(updateCommand)
        except Exception as e:
            pritn(e)

        return(output)

    except Exception as e:
        print(e)


# SMTP log in information
mail = Mail("mail.messagingengine.com",
            port=465, username="aschoonover@fastmail.fm",
            password="MkaV3yYevpvKqbT2RarY",
            use_tls=False, use_ssl=True, debug_level=None)

# email message object
msg = Message(fromaddr=("Adam Elchert", "adam@elchert.net"))

# attachment
with open('fileOutput.txt') as fileOutput:
    attachment = fileOutput.read()

fileOutput.close()

# update message object
msg.fromaddr = ("adam@elchert.net")
msg.body= '{}'.format(attachment)
msg.to = ('adam@elchert.net')
msg.subject=('Tweets from{}'.format(strftime('%B %d')))
mail.send(msg)

updateFile()
