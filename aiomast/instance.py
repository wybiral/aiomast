class InstanceAPI:
    '''
    Instance related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def info(self):
        '''
        Obtain general information about the server.
        https://docs.joinmastodon.org/methods/instance/#v2
        '''
        path = '/api/v2/instance'
        return await self.api._get(path)

    async def peers(self):
        '''
        Domains that this instance is aware of.
        https://docs.joinmastodon.org/methods/instance/#peers
        '''
        path = '/api/v1/instance/peers'
        return await self.api._get(path)

    async def activity(self):
        '''
        Instance activity over the last 3 months, binned weekly.
        https://docs.joinmastodon.org/methods/instance/#activity
        '''
        path = '/api/v1/instance/activity'
        return await self.api._get(path)

    async def rules(self):
        '''
        Rules that the users of this service should follow.
        https://docs.joinmastodon.org/methods/instance/#rules
        '''
        path = '/api/v1/instance/rules'
        return await self.api._get(path)

    async def domain_blocks(self):
        '''
        Obtain a list of domains that have been blocked.
        https://docs.joinmastodon.org/methods/instance/#domain_blocks
        '''
        path = '/api/v1/instance/domain_blocks'
        return await self.api._get(path)

    async def extended_description(self):
        '''
        Obtain an extended description of this server.
        https://docs.joinmastodon.org/methods/instance/#extended_description
        '''
        path = '/api/v1/instance/extended_description'
        return await self.api._get(path)

    async def directory(self, **query):
        '''
        List accounts visible in the directory.
        https://docs.joinmastodon.org/methods/directory/#get
        '''
        path = '/api/v1/directory'
        return await self.api._get(path, query=query)

    async def custom_emojis(self):
        '''
        Returns custom emojis that are available on the server.
        https://docs.joinmastodon.org/methods/custom_emojis/#get
        '''
        path = '/api/v1/custom_emojis'
        return await self.api._get(path)

    async def search(self, q, **query):
        '''
        Search for content in accounts, statuses and hashtags.
        https://docs.joinmastodon.org/methods/search/#v2
        '''
        path = '/api/v2/search'
        query['q'] = q
        return await self.api._get(path, query=query)
