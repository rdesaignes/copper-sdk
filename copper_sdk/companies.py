from copper_sdk.base import BaseResource


class Companies(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/companies/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/companies', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/companies/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/companies/{id}")

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
            'sort_by': 'date_modified',  # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }
        return self.copper.post('/companies/search', {**default_body, **body})

    def all(self, page_number=1, page_size=200):
        keep_going = True
        all_items = []
        while keep_going is True :
            body = {
                'page_number': page_number,
                'page_size': page_size,
                'sort_by': 'name',
                'sort_direction': 'asc'
            }
            items_list = self.list(body)
            page_number += 1
            if len(items_list) > 0:
                all_items += items_list
            else: keep_going = False
        return all_items

    def list_related(self, id):
        return self.copper.get(f'/companies/{id}/related')

    def activities(self, id):
        return self.copper.get(f"/companies/{id}/activities")

    def contact_types(self):
        return self.copper.get('/contact_types')
