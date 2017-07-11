from sender import Message
from sender import Mail
from sender import Attachment


# https://sender.readthedocs.io/

msg = Message("testing html", fromaddr="adam@elchert.net",
              to="adam@elchert.net")

mail = Mail("mail.messagingengine.com",
            port=465, username="aschoonover@fastmail.fm",
            password="MkaV3yYevpvKqbT2RarY",
            use_tls=False, use_ssl=True, debug_level=None)

#open html file to print to body
with open('testFile.html', 'r') as f:
    data = f.read()

f.close()

msg.html = data

mail.send(msg)
