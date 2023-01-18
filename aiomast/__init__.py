from aiohttp import ClientSession

from .accounts import AccountsAPI
from .bookmarks import BookmarksAPI
from .conversations import ConversationsAPI
from .favourites import FavouritesAPI
from .instance import InstanceAPI
from .lists import ListsAPI
from .mutes import MutesAPI
from .notifications import NotificationsAPI
from .statuses import StatusesAPI
from .timelines import TimelinesAPI
from .trends import TrendsAPI
from .websockets import WebSocketsAPI


class MastodonAPI:
    '''
    Minimal asynchronous wrapper for Mastodon API.
    '''
    def __init__(self, url, ssl=None):
        self.url = _normalize_url(url)
        # SSL context (default context used if None)
        self.ssl = ssl
        self.session = ClientSession()
        self.accounts = AccountsAPI(self)
        self.bookmarks = BookmarksAPI(self)
        self.conversations = ConversationsAPI(self)
        self.favourites = FavouritesAPI(self)
        self.instance = InstanceAPI(self)
        self.lists = ListsAPI(self)
        self.mutes = MutesAPI(self)
        self.notifications = NotificationsAPI(self)
        self.statuses = StatusesAPI(self)
        self.timelines = TimelinesAPI(self)
        self.trends = TrendsAPI(self)
        self.websockets = WebSocketsAPI(self)

    def set_access_token(self, access_token):
        '''
        Set OAuth access token.
        '''
        self.session.headers['Authorization'] = f'Bearer {access_token}'

    async def _request(self, method, path, query=None, body=None):
        '''
        Perform HTTP request using method for API path and return parsed JSON.
        '''
        url = self.url + path
        kwargs = {}
        if self.ssl is not None:
            kwargs['ssl'] = self.ssl
        if query is not None:
            kwargs['params'] = query
        if body is not None:
            kwargs['json'] = body
        async with self.session.request(method, url, **kwargs) as resp:
            return await resp.json()

    async def _get(self, path, **kwargs):
        '''
        Perform GET request for API path and return parsed JSON.
        '''
        return await self._request('GET', path, **kwargs)

    async def _post(self, path, **kwargs):
        '''
        Perform POST request for API path and return parsed JSON.
        '''
        return await self._request('POST', path, **kwargs)

    async def _put(self, path, **kwargs):
        '''
        Perform PUT request for API path and return parsed JSON.
        '''
        return await self._request('PUT', path, **kwargs)

    async def _delete(self, path, **kwargs):
        '''
        Perform DELETE request for API path and return parsed JSON.
        '''
        return await self._request('DELETE', path, **kwargs)

    async def _websocket(self, path, streaming_url=None):
        '''
        Perform a WebSocket request for API path and return connection.
        '''
        if streaming_url is None:
            _, streaming_url = self.url.split('://', maxsplit=1)
            streaming_url = 'wss://' + streaming_url
        url = streaming_url + path
        return await self.session.ws_connect(url, ssl=self.ssl)

    async def close(self):
        await self.session.close()

    async def __aenter__(self, *args):
        return self

    async def __aexit__(self, *args):
        await self.close()


def _normalize_url(url):
    url = url.rstrip('/')
    if url.startswith('http://'):
        return url
    if url.startswith('https://'):
        return url
    return 'https://' + url
