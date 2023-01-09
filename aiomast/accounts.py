class AccountsAPI:
    '''
    Account related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def verify_credentials(self):
        '''
        Test to make sure that the user token works.
        https://docs.joinmastodon.org/methods/accounts/#verify_credentials
        '''
        path = '/api/v1/accounts/verify_credentials'
        return await self.api._get(path)

    async def get(self, id):
        '''
        View information about a profile.
        https://docs.joinmastodon.org/methods/accounts/#get
        '''
        path = f'/api/v1/accounts/{id}'
        return await self.api._get(path)

    async def statuses(self, id, **query):
        '''
        Statuses posted to the given account.
        https://docs.joinmastodon.org/methods/accounts/#statuses
        '''
        path = f'/api/v1/accounts/{id}/statuses'
        return await self.api._get(path, query=query)

    async def followers(self, id, **query):
        '''
        Accounts which follow given account, if network isn't hidden.
        https://docs.joinmastodon.org/methods/accounts/#followers
        '''
        path = f'/api/v1/accounts/{id}/followers'
        return await self.api._get(path, query=query)

    async def following(self, id, **query):
        '''
        Accounts which the given account follows, if network isn't hidden.
        https://docs.joinmastodon.org/methods/accounts/#following
        '''
        path = f'/api/v1/accounts/{id}/following'
        return await self.api._get(path, query=query)

    async def featured_tags(self, id):
        '''
        Tags featured by this account.
        https://docs.joinmastodon.org/methods/accounts/#featured_tags
        '''
        path = f'/api/v1/accounts/{id}/featured_tags'
        return await self.api._get(path)

    async def lists(self, id):
        '''
        User lists that you have added this account to.
        https://docs.joinmastodon.org/methods/accounts/#lists
        '''
        path = f'/api/v1/accounts/{id}/lists'
        return await self.api._get(path)

    async def follow(self, id, **body):
        '''
        Follow the given account.
        Can also update whether to show reblogs or enable notifications.
        https://docs.joinmastodon.org/methods/accounts/#follow
        '''
        path = f'/api/v1/accounts/{id}/follow'
        return await self.api._post(path, body=body)

    async def unfollow(self, id):
        '''
        Unfollow the given account.
        https://docs.joinmastodon.org/methods/accounts/#unfollow
        '''
        path = f'/api/v1/accounts/{id}/unfollow'
        return await self.api._post(path)

    async def remove_from_followers(self, id):
        '''
        Remove the given account from your followers.
        https://docs.joinmastodon.org/methods/accounts/#remove_from_followers
        '''
        path = f'/api/v1/accounts/{id}/remove_from_followers'
        return await self.api._post(path)

    async def block(self, id):
        '''
        Block the given account.
        https://docs.joinmastodon.org/methods/accounts/#block
        '''
        path = f'/api/v1/accounts/{id}/block'
        return await self.api._post(path)

    async def unblock(self, id):
        '''
        Unblock the given account.
        https://docs.joinmastodon.org/methods/accounts/#unblock
        '''
        path = f'/api/v1/accounts/{id}/unblock'
        return await self.api._post(path)

    async def mute(self, id):
        '''
        Mute the given account.
        https://docs.joinmastodon.org/methods/accounts/#mute
        '''
        path = f'/api/v1/accounts/{id}/mute'
        return await self.api._post(path)

    async def unmute(self, id):
        '''
        Unmute the given account.
        https://docs.joinmastodon.org/methods/accounts/#unmute
        '''
        path = f'/api/v1/accounts/{id}/unmute'
        return await self.api._post(path)

    async def pin(self, id):
        '''
        Add the given account to the user’s featured profiles.
        https://docs.joinmastodon.org/methods/accounts/#pin
        '''
        path = f'/api/v1/accounts/{id}/pin'
        return await self.api._post(path)

    async def unpin(self, id):
        '''
        Remove the given account from the user’s featured profiles.
        https://docs.joinmastodon.org/methods/accounts/#unpin
        '''
        path = f'/api/v1/accounts/{id}/unpin'
        return await self.api._post(path)

    async def note(self, id, text):
        '''
        Sets a private note on a user.
        https://docs.joinmastodon.org/methods/accounts/#note
        '''
        path = f'/api/v1/accounts/{id}/note'
        body = {'comment': text}
        return await self.api._post(path, body=body)

    async def relationships(self, *ids):
        '''
        Find out whether a given account is followed, blocked, muted, etc.
        https://docs.joinmastodon.org/methods/accounts/#relationships
        '''
        path = '/api/v1/accounts/relationships'
        query = '&'.join(f'id[]={id}' for id in ids)
        return await self.api._get(path + '?' + query)

    async def familiar_followers(self, *ids):
        '''
        Obtain a list of all accounts that follow a given account,
        filtered for accounts you follow.
        https://docs.joinmastodon.org/methods/accounts/#familiar_followers
        '''
        path = '/api/v1/accounts/familiar_followers'
        query = '&'.join(f'id[]={id}' for id in ids)
        return await self.api._get(path + '?' + query)

    async def search(self, q, **query):
        '''
        Search for matching accounts by username or display name.
        https://docs.joinmastodon.org/methods/accounts/#search
        '''
        path = '/api/v1/accounts/search'
        query['q'] = q
        return await self.api._get(path, query=query)

    async def lookup(self, acct):
        '''
        Quickly lookup a username to see if it is available,
        skipping WebFinger resolution.
        https://docs.joinmastodon.org/methods/accounts/#lookup
        '''
        path = '/api/v1/accounts/lookup'
        return await self.api._get(path, query={'acct': acct})
