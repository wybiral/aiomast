class BookmarksAPI:
    '''
    Bookmarks related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        Statuses the user has bookmarked.
        https://docs.joinmastodon.org/methods/bookmarks/#get
        '''
        path = '/api/v1/bookmarks'
        return await self.api._get(path, query=query)
