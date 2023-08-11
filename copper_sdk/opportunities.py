from copper_sdk.base import BaseResource


class Opportunities(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/opportunities/{id}")

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/opportunities', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f"/opportunities/{id}", body)

    def delete(self, id):
        return self.copper.delete(f"/opportunities/{id}")

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            'page_number': 1,  # number	The page number (starting with 1) that you would like to view.
            'page_size': 20,  # number	The number of entries included in a page of results
            'sort_by': 'name',  # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }
        return self.copper.post('/opportunities/search', {**default_body, **body})

    def all(self, page_number=1, page_size=200):
        keep_going = True
        all_items = []
        while keep_going is True :
            body = {
                'page_number': page_number,
                'page_size': page_size
            }
            items_list = self.list(body)
            page_number += 1
            if len(items_list) > 0:
                all_items += items_list
            else: keep_going = False
        return all_items

    def customer_sources(self):
        return self.copper.get('/customer_sources')

    def loss_reasons(self):
        return self.copper.get('/loss_reasons')

    def pipelines(self):
        return self.copper.get('/pipelines')

    def pipeline_stages(self):
        return self.copper.get('/pipeline_stages')

    def stages_in_pipeline(self, id):
        return self.copper.get(f'/pipeline/pipeline_stages/{id}')

    def related(self, id):
        return self.copper.get(f'/opportunities/{id}/related')

