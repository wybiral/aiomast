class MutesAPI:
    '''
    Mutes related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        Accounts the user has muted.
        https://docs.joinmastodon.org/methods/mutes/#get
        '''
        path = '/api/v1/mutes'
        return await self.api._get(path, query=query)
