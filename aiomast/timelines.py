class TimelinesAPI:
    '''
    Timeline related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def public(self, **query):
        '''
        View public statuses.
        https://docs.joinmastodon.org/methods/timelines/#public
        '''
        path = '/api/v1/timelines/public'
        return await self.api._get(path, query=query)

    async def hashtag(self, tag, **query):
        '''
        View public statuses containing the given hashtag.
        https://docs.joinmastodon.org/methods/timelines/#tag
        '''
        path = f'/api/v1/timelines/tag/{tag}'
        return await self.api._get(path, query=query)

    async def home(self, **query):
        '''
        View statuses from followed users.
        https://docs.joinmastodon.org/methods/timelines/#home
        '''
        path = '/api/v1/timelines/home'
        return await self.api._get(path, query=query)

    async def list(self, id, **query):
        '''
        View statuses in the given list timeline.
        https://docs.joinmastodon.org/methods/timelines/#list
        '''
        path = f'/api/v1/timelines/list/{id}'
        return await self.api._get(path, query=query)
