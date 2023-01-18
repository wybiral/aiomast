class BlocksAPI:
    '''
    Blocks related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        View blocked users.
        https://docs.joinmastodon.org/methods/blocks/#get
        '''
        path = '/api/v1/blocks'
        return await self.api._get(path, query=query)
