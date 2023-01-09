from aiohttp import WSMsgType
import json


class WebSocketsAPI:
    '''
    WebSockets API endpoint for streaming data.
    '''
    def __init__(self, api):
        self.api = api

    async def connect(self, streaming_url=None):
        '''
        Create WebSocket connection to streaming API.
        '''
        path = '/api/v1/streaming'
        ws = await self.api._websocket(path, streaming_url=streaming_url)
        return WebSocket(ws)


class WebSocket:

    def __init__(self, ws):
        self._ws = ws

    async def __aiter__(self):
        async for msg in self._ws:
            if msg.type == WSMsgType.TEXT:
                event = json.loads(msg.data)
                if 'payload' in event:
                    event['data'] = json.loads(event['payload'])
                    del event['payload']
                yield event
            elif msg.type == WSMsgType.ERROR:
                break

    async def subscribe(self, stream, **kwargs):
        kwargs['type'] = 'subscribe'
        kwargs['stream'] = stream
        await self._ws.send_str(json.dumps(kwargs))
