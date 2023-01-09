class ListsAPI:
    '''
    List related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self):
        '''
        Fetch all lists that the user owns.
        https://docs.joinmastodon.org/methods/lists/#get
        '''
        path = '/api/v1/lists'
        return await self.api._get(path)

    async def get(self, id):
        '''
        Fetch the list with the given ID.
        https://docs.joinmastodon.org/methods/lists/#get-one
        '''
        path = f'/api/v1/lists/{id}'
        return await self.api._get(path)

    async def create(self, title, replies_policy='list'):
        '''
        Create a new list.
        https://docs.joinmastodon.org/methods/lists/#create
        '''
        path = '/api/v1/lists'
        query = {'title': title, 'replies_policy': replies_policy}
        return await self.api._post(path, query=query)

    async def update(self, id, **query):
        '''
        Change the title of a list, or which replies to show.
        https://docs.joinmastodon.org/methods/lists/#update
        '''
        path = f'/api/v1/lists/{id}'
        return await self.api._put(path, query=query)

    async def delete(self, id):
        '''
        Delete a list.
        https://docs.joinmastodon.org/methods/lists/#delete
        '''
        path = f'/api/v1/lists/{id}'
        return await self.api._delete(path)

    async def accounts(self, id, **query):
        '''
        View accounts in a list.
        https://docs.joinmastodon.org/methods/lists/#accounts
        '''
        path = f'/api/v1/lists/{id}/accounts'
        return await self.api._get(path, query=query)

    async def add_accounts(self, id, *account_ids):
        '''
        Add accounts to the given list.
        Note that the user must be following these accounts.
        https://docs.joinmastodon.org/methods/lists/#accounts-add
        '''
        path = f'/api/v1/lists/{id}/accounts'
        query = {'account_ids': account_ids}
        return await self.api._post(path, query=query)

    async def remove_accounts(self, id, *account_ids):
        '''
        Remove accounts from the given list.
        https://docs.joinmastodon.org/methods/lists/#accounts-add
        '''
        path = f'/api/v1/lists/{id}/accounts'
        query = {'account_ids': account_ids}
        return await self.api._delete(path, query=query)
