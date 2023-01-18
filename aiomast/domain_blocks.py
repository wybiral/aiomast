class DomainBlocksAPI:
    '''
    Domain blocks related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        View domains the user has blocked.
        https://docs.joinmastodon.org/methods/domain_blocks/#get
        '''
        path = '/api/v1/domain_blocks'
        return await self.api._get(path, query=query)

    async def block(self, domain, **body):
        '''
        Block a domain.
        https://docs.joinmastodon.org/methods/domain_blocks/#block
        '''
        path = '/api/v1/domain_blocks'
        body['domain'] = domain
        return await self.api._post(path, body=body)

    async def unblock(self, domain, **body):
        '''
        Remove a domain block.
        https://docs.joinmastodon.org/methods/domain_blocks/#unblock
        '''
        path = '/api/v1/domain_blocks'
        body['domain'] = domain
        return await self.api._delete(path, body=body)
