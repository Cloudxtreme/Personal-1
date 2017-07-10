from sender import Message
from sender import Mail
from sender import Attachment


# https://sender.readthedocs.io/

msg = Message("demo subject", fromaddr="adam@elchert.net",
              to="adam@elchert.net")

msg.body = "demo body"

mail = Mail("mail.messagingengine.com",
            port=465, username="aschoonover@fastmail.fm",
            password="MkaV3yYevpvKqbT2RarY",
            use_tls=False, use_ssl=True, debug_level=None)

mail.send(msg)
msg.html.close()
