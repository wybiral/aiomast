class FiltersAPI:
    '''
    Filters related API endpoints.
    '''
    def __init__(self, api):
        self.api = api

    async def all(self, **query):
        '''
        Obtain a list of all filter groups for the current user.
        https://docs.joinmastodon.org/methods/filters/#get
        '''
        path = '/api/v2/filters'
        return await self.api._get(path, query=query)

    async def get(self, id, **query):
        '''
        Obtain a single filter group owned by the current user.
        https://docs.joinmastodon.org/methods/filters/#get-one
        '''
        path = f'/api/v2/filters/{id}'
        return await self.api._get(path, query=query)

    async def create(self, title, context='home', **body):
        '''
        Create a filter group with the given parameters.
        https://docs.joinmastodon.org/methods/filters/#create
        '''
        path = '/api/v2/filters'
        body['title'] = title
        if isinstance(context, str):
            context = [context]
        body['context'] = context
        return await self.api._post(path, body=body)

    async def update(self, id, **body):
        '''
        Update a filter group with the given parameters.
        https://docs.joinmastodon.org/methods/filters/#update
        '''
        path = f'/api/v2/filters/{id}'
        return await self.api._put(path, body=body)

    async def delete(self, id, **body):
        '''
        Delete a filter group with the given id.
        https://docs.joinmastodon.org/methods/filters/#delete
        '''
        path = f'/api/v2/filters/{id}'
        return await self.api._delete(path, body=body)

    async def keywords(self, id, **query):
        '''
        List all keywords attached to the current filter group.
        https://docs.joinmastodon.org/methods/filters/#keywords-get
        '''
        path = f'/api/v2/filters/{id}/keywords'
        return await self.api._get(path, query=query)

    async def create_keyword(self, id, keyword, **body):
        '''
        Add the given keyword to the specified filter group.
        https://docs.joinmastodon.org/methods/filters/#keywords-create
        '''
        path = f'/api/v2/filters/{id}/keywords'
        body['keyword'] = keyword
        return await self.api._post(path, body=body)

    async def get_keyword(self, id, **query):
        '''
        Get one filter keyword by the given id.
        https://docs.joinmastodon.org/methods/filters/#keywords-get-one
        '''
        path = f'/api/v2/filters/keywords/{id}'
        return await self.api._get(path, query=query)

    async def update_keyword(self, id, **body):
        '''
        Update the given filter keyword.
        https://docs.joinmastodon.org/methods/filters/#keywords-update
        '''
        path = f'/api/v2/filters/keywords/{id}'
        return await self.api._put(path, body=body)

    async def delete_keyword(self, id, **body):
        '''
        Deletes the given filter keyword.
        https://docs.joinmastodon.org/methods/filters/#keywords-delete
        '''
        path = f'/api/v2/filters/keywords/{id}'
        return await self.api._delete(path, body=body)

    async def status_filters(self, id, **query):
        '''
        Obtain a list of all status filters within this filter group.
        https://docs.joinmastodon.org/methods/filters/#statuses-get
        '''
        path = f'/api/v2/filters/{id}/statuses'
        return await self.api._get(path, query=query)

    async def create_status_filter(self, id, status_id, **body):
        '''
        Add a status filter to the current filter group.
        https://docs.joinmastodon.org/methods/filters/#statuses-add
        '''
        path = f'/api/v2/filters/{id}/statuses'
        body['status_id'] = status_id
        return await self.api._post(path, body=body)

    async def get_status_filter(self, id, **query):
        '''
        Obtain a single status filter.
        https://docs.joinmastodon.org/methods/filters/#statuses-get-one
        '''
        path = f'/api/v2/filters/statuses/{id}'
        return await self.api._get(path, query=query)

    async def delete_status_filter(self, id, **body):
        '''
        Remove a status filter from the current filter group.
        https://docs.joinmastodon.org/methods/filters/#statuses-remove
        '''
        path = f'/api/v2/filters/statuses/{id}'
        return await self.api._delete(path, body=body)
