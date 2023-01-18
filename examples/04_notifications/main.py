'''
Demonstrate listing notifications.

This requires the environment variable MASTODON_TOKEN to be set to a private
access token (this doesn't do the OAuth side of things for you yet).
'''

import asyncio
import certifi
import json
import os
import ssl

from aiomast import MastodonAPI

MASTODON_INSTANCE = 'mastodon.social'
ACCESS_TOKEN = os.environ['MASTODON_TOKEN']

async def main():
    # provide SSL context (optional)
    ssl_ctx = ssl.create_default_context(cafile=certifi.where())
    # create API instance with context manager
    async with MastodonAPI(MASTODON_INSTANCE, ssl=ssl_ctx) as m:
        # set OAuth access token
        m.set_access_token(ACCESS_TOKEN)
        # get all notifications
        notifications = await m.notifications.all()
        print(json.dumps(notifications, indent='  '))

asyncio.run(main())