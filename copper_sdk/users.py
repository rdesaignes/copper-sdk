from copper_sdk.base import BaseResource


class Users(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f"/users/{id}")

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
        }
        return self.copper.post('/users/search', {**default_body, **body})

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