class FollowRequestsAPI:
    '''
    Follow requests related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        View pending follow requests.
        https://docs.joinmastodon.org/methods/follow_requests/#get
        '''
        path = '/api/v1/follow_requests'
        return await self.api._get(path, query=query)

    async def accept(self, id, **body):
        '''
        Accept follow request.
        https://docs.joinmastodon.org/methods/follow_requests/#accept
        '''
        path = f'/api/v1/follow_requests/{id}/authorize'
        return await self.api._post(path, body=body)

    async def reject(self, id, **body):
        '''
        Reject follow request.
        https://docs.joinmastodon.org/methods/follow_requests/#reject
        '''
        path = f'/api/v1/follow_requests/{id}/authorize'
        return await self.api._post(path, body=body)
