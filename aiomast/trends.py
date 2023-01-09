class TrendsAPI:
    '''
    Trends related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def tags(self, **query):
        '''
        Tags that are being used more frequently within the past week.
        https://docs.joinmastodon.org/methods/trends/#tags
        '''
        path = '/api/v1/trends/tags'
        return await self.api._get(path, query=query)

    async def statuses(self, **query):
        '''
        Statuses that have been interacted with more than others.
        https://docs.joinmastodon.org/methods/trends/#statuses
        '''
        path = '/api/v1/trends/statuses'
        return await self.api._get(path, query=query)

    async def links(self, **query):
        '''
        Links that have been shared more than others.
        https://docs.joinmastodon.org/methods/trends/#links
        '''
        path = '/api/v1/trends/links'
        return await self.api._get(path, query=query)
