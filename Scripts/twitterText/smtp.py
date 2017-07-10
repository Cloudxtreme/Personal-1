from sender import Message
from sender import Mail


# https://sender.readthedocs.io/

msg = Message("demo subject", fromaddr="adam@elchert.net",
              to="adam@elchert.net")

msg.body = "demo body"
msg.html = "<h1>Body test</h1>"

mail = Mail("mail.messagingengine.com", port=465, username="aschoonover@fastmail.fm", password="MkaV3yYevpvKqbT2RarY",
            use_tls=False, use_ssl=True, debug_level=None)

mail.send(msg)
