class StatusesAPI:
    '''
    Status related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def post(self, status, **query):
        '''
        Publish a status with the given parameters.
        https://docs.joinmastodon.org/methods/statuses/#create
        '''
        path = '/api/v1/statuses'
        query['status'] = status
        return await self.api._post(path, query=query)

    async def get(self, id):
        '''
        Obtain information about a status.
        https://docs.joinmastodon.org/methods/statuses/#get
        '''
        path = f'/api/v1/statuses/{id}'
        return await self.api._get(path)

    async def delete(self, id):
        '''
        Delete one of your own statuses.
        https://docs.joinmastodon.org/methods/statuses/#delete
        '''
        path = f'/api/v1/statuses/{id}'
        return await self.api._delete(path)

    async def context(self, id):
        '''
        View statuses above and below this status in the thread.
        https://docs.joinmastodon.org/methods/statuses/#context
        '''
        path = f'/api/v1/statuses/{id}/context'
        return await self.api._get(path)

    async def get_boosts(self, id, **query):
        '''
        View who boosted a given status.
        https://docs.joinmastodon.org/methods/statuses/#reblogged_by
        '''
        path = f'/api/v1/statuses/{id}/reblogged_by'
        return await self.api._get(path, query=query)

    async def get_favourites(self, id, **query):
        '''
        View who favourited a given status.
        https://docs.joinmastodon.org/methods/statuses/#favourited_by
        '''
        path = f'/api/v1/statuses/{id}/favourited_by'
        return await self.api._get(path, query=query)

    async def favourite(self, id):
        '''
        Add a status to your favourites list.
        https://docs.joinmastodon.org/methods/statuses/#favourite
        '''
        path = f'/api/v1/statuses/{id}/favourite'
        return await self.api._post(path)

    async def unfavourite(self, id):
        '''
        Remove a status from your favourites list.
        https://docs.joinmastodon.org/methods/statuses/#unfavourite
        '''
        path = f'/api/v1/statuses/{id}/unfavourite'
        return await self.api._post(path)

    async def boost(self, id):
        '''
        Reshare a status on your own profile.
        https://docs.joinmastodon.org/methods/statuses/#boost
        '''
        path = f'/api/v1/statuses/{id}/reblog'
        return await self.api._post(path)

    async def unboost(self, id):
        '''
        Undo a reshare of a status.
        https://docs.joinmastodon.org/methods/statuses/#unreblog
        '''
        path = f'/api/v1/statuses/{id}/unreblog'
        return await self.api._post(path)

    async def bookmark(self, id):
        '''
        Privately bookmark a status.
        https://docs.joinmastodon.org/methods/statuses/#bookmark
        '''
        path = f'/api/v1/statuses/{id}/bookmark'
        return await self.api._post(path)

    async def unbookmark(self, id):
        '''
        Remove a status from your private bookmarks.
        https://docs.joinmastodon.org/methods/statuses/#unbookmark
        '''
        path = f'/api/v1/statuses/{id}/unbookmark'
        return await self.api._post(path)

    async def mute(self, id):
        '''
        Do not receive notifications for thread this status is part of.
        Must be a thread in which you are a participant.
        https://docs.joinmastodon.org/methods/statuses/#mute
        '''
        path = f'/api/v1/statuses/{id}/mute'
        return await self.api._post(path)

    async def unmute(self, id):
        '''
        Start receiving notifications again for thread this status is part of.
        https://docs.joinmastodon.org/methods/statuses/#unmute
        '''
        path = f'/api/v1/statuses/{id}/unmute'
        return await self.api._post(path)

    async def pin(self, id):
        '''
        Feature one of your own public statuses at the top of your profile.
        https://docs.joinmastodon.org/methods/statuses/#pin
        '''
        path = f'/api/v1/statuses/{id}/pin'
        return await self.api._post(path)

    async def unpin(self, id):
        '''
        Unfeature a status from the top of your profile.
        https://docs.joinmastodon.org/methods/statuses/#unpin
        '''
        path = f'/api/v1/statuses/{id}/unpin'
        return await self.api._post(path)

    async def edit(self, id, **body):
        '''
        Edit status to change text, sensitivity, media attachments, or poll.
        Note that editing a poll's options will reset the votes.
        https://docs.joinmastodon.org/methods/statuses/#edit
        '''
        path = f'/api/v1/statuses/{id}'
        return await self.api._put(path, body=body)

    async def get_history(self, id):
        '''
        Get all known versions of status, including initial and current states.
        https://docs.joinmastodon.org/methods/statuses/#history
        '''
        path = f'/api/v1/statuses/{id}/history'
        return await self.api._get(path)

    async def get_source(self, id):
        '''
        Obtain the source properties for a status so that it can be edited.
        https://docs.joinmastodon.org/methods/statuses/#source
        '''
        path = f'/api/v1/statuses/{id}/source'
        return await self.api._get(path)
