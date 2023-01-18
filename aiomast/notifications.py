class NotificationsAPI:
    '''
    Notifications related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        Notifications concerning the user.
        https://docs.joinmastodon.org/methods/notifications/#get
        '''
        path = '/api/v1/notifications'
        return await self.api._get(path, query=query)

    async def get(self, id, **query):
        '''
        View information about a notification with a given ID.
        https://docs.joinmastodon.org/methods/notifications/#get-one
        '''
        path = f'/api/v1/notifications/{id}'
        return await self.api._get(path, query=query)

    async def clear(self, **query):
        '''
        Clear all notifications from the server.
        https://docs.joinmastodon.org/methods/notifications/#clear
        '''
        path = '/api/v1/notifications/clear'
        return await self.api._post(path, query=query)

    async def dismiss(self, id, **query):
        '''
        Dismiss a single notification from the server.
        https://docs.joinmastodon.org/methods/notifications/#dismiss
        '''
        path = f'/api/v1/notifications/{id}/dismiss'
        return await self.api._post(path, query=query)
