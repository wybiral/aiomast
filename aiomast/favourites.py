class FavouritesAPI:
    '''
    Favourites related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        Statuses the user has favourited.
        https://docs.joinmastodon.org/methods/favourites/#get
        '''
        path = '/api/v1/favourites'
        return await self.api._get(path, query=query)
