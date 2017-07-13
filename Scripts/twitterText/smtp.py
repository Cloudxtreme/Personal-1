from sender import Message
from sender import Mail
from sender import Attachment

mail = Mail("mail.messagingengine.com",
            port=465, username="aschoonover@fastmail.fm",
            password="MkaV3yYevpvKqbT2RarY",
            use_tls=False, use_ssl=True, debug_level=None)

msg = Message("Hello", fromaddr=("Adam Elchert", "adam@elchert.net"))

with open('fileOutput.txt') as fo:
    attachment = fo.read()

fo.close()
msg.fromaddr = ("adam@elchert.net")
msg.body= '{}'.format(attachment)
msg.to = ('adam@elchert.net')
mail.send(msg)

#sqlite3 -column tweets.db 'select username, tweetText, tweetURL from tweets;' > fileOutput.txt
