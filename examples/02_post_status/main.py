'''
Demonstrate posting a status.

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
        # verify that access token works
        verify = await m.accounts.verify_credentials()
        if 'error' in verify:
            print(verify['error'])
            return
        # post status (by setting visibility='direct' you post it as a direct
        # message to anyone mentioned, in this case only ourself, you can
        # change this to 'public', 'unlisted', or 'private' too)
        status = await m.statuses.post('Hello world!', visibility='direct')
        # print result to see that it posted
        print(json.dumps(status, indent='  '))

asyncio.run(main())