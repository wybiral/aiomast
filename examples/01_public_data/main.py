'''
Demonstrate basic API requests from an instance using MastodonAPI interface.
'''

import asyncio
import certifi
import json
import ssl

from aiomast import MastodonAPI

MASTODON_INSTANCE = 'mastodon.social'

async def main():
    # provide SSL context (optional)
    ssl_ctx = ssl.create_default_context(cafile=certifi.where())
    # create API instance with context manager
    async with MastodonAPI(MASTODON_INSTANCE, ssl=ssl_ctx) as m:
        # grab instance info
        print('Instance info:')
        info = await m.instance.info()
        print(json.dumps(info, indent='  '))
        print('')
        # lookup account
        print('Account info:')
        account = await m.accounts.lookup('davywtf')
        print(json.dumps(account, indent='  '))
        print('')
        # get trending hashtags
        print('Trending hashtags:')
        hashtags = await m.trends.tags()
        print(json.dumps(hashtags, indent='  '))
        print('')


asyncio.run(main())