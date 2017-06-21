#!/usr/bin/env python
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from imgurpython import *

import os

client_id = '47a9dbfd913259b'
client_secret = 'a3baf6d553e892ecf5c9fd7459296d97bc9c5fb4'

client = ImgurClient(client_id, client_secret)

# Example request
# items = client.gallery()
account_info = client.get_account(nonstopflights)

try:
    for i in account_info:
        print i

except:
    print(ImgurClientError.error_message)
    print(ImgurClientError.status_code)
