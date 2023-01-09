'''
Demonstrate streaming public data from the instance in real-time.
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
        # create websocket connection
        stream = await m.websockets.connect()
        # subscribe to 'public:local:media' (media posts on local instance)
        await stream.subscribe('public:local:media')
        # print real-time activity from the stream
        async for msg in stream:
            print(json.dumps(msg, indent='  '))
            print('')

asyncio.run(main())