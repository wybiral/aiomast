class ConversationsAPI:
    '''
    Conversation related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        View all conversations.
        https://docs.joinmastodon.org/methods/conversations/#get
        '''
        path = '/api/v1/conversations'
        return await self.api._get(path, query=query)

    async def remove(self, id):
        '''
        Removes a conversation from your list of conversations.
        https://docs.joinmastodon.org/methods/conversations/#delete
        '''
        path = f'/api/v1/conversations/{id}'
        return await self.api._delete(path)

    async def read(self, id):
        '''
        Mark a conversation as read.
        https://docs.joinmastodon.org/methods/conversations/#read
        '''
        path = f'/api/v1/conversations/{id}/read'
        return await self.api._post(path)
