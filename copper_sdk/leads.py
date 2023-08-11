from copper_sdk.base import BaseResource


class Leads(BaseResource):

    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get(f'/leads/{id}')

    def create(self, body=None):
        if body is None:
            body = {}
        return self.copper.post('/leads', body)

    def update(self, id, body=None):
        if body is None:
            body = {}
        return self.copper.put(f'/leads/{id}', body)

    def delete(self, id):
        return self.copper.delete(f'/leads/{id}')

    def upsert(self, body=None):
        if body is None:
            body = {}
        return self.copper.put('/leads/upsert', body)

    def convert(self, id, body=None):
        if body is None:
            body = {}
        default_body = {
            "details": {
                'person': {}, # object	Details about the Person to be created by the Lead conversion. Valid fields are name, contact_type_id, and assignee_id.
                'company': {}, # object	Details about the Company to which the newly created Person will belong. Valid fields are id or name, and they are mutually exclusive. If a Company id is specified, the new Person will belong to that Company. If the name of an existing Company is specified, the new Person will belong to that Company. If a new name is specified, a new Company will be created with that name, and the new Person will belong to that Company. If you explicitly supply an empty string ("") for the company name, then no Company will be created. By default, fuzzy matching will return a list of candidate companies. An optional Boolean field "exact_match" can be specified if the exact company name is known.
                'opportunity': {}, # object	Details about the Opportunity to be created by the Lead conversion. Valid fields are name, pipeline_id, pipeline_stage_id, 'monetary_value, and assignee_id. If unspecified, no Opportunity will be created. If pipeline_stage_id is unspecified, it will default to the first stage in the pipeline.
            }
        }

        url = f"/leads/{id}/convert"
        payload = { **default_body, **body }
        return self.copper.post(f"/leads/{id}/convert", payload)

    def list(self, body=None):
        if body is None:
            body = {}
        default_body = {
            'page_number': 1,  # number	The page number (starting with 1) that you would like to view.
            'page_size': 20,  # number	The number of entries included in a page of results
            'sort_by': 'name',  # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }
        return self.copper.post('/leads/search', { **default_body, **body})

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

    def activities(self, id, body=None):
        if body is None:
            body = {}
        default_body = {
            'page_number': 1, # number	The page number (starting with 1) that you would like to view.	1
            'page_size': 20, # number	The number of entries included in a page of results	20
            'full_result': False, # boolean	(Optional) If set to true, search performance improves but duplicate activity logs may be returned (footnote 3).	false
        }
        return self.copper.post(f'/leads/{id}/activities', {**default_body, **body})

    def customer_sources(self):
        return self.copper.get('/customer_sources')

    def statuses(self):
        return self.copper.get('/lead_statuses')

    def list_related(self, id):
        return self.copper.get(f'/related_links?source_type=lead&source_id={id}')

    def unrelate(self, id):
        return self.copper.delete(f'/related_links/{id}')

    def relate(self, relation_id, id, target_type, target_id):
        body = {
            'custom_field_definition_id': relation_id, 
            'source': {
                'id': id,
                'entity_type': 'lead'
            },
            'target': {
                'id': target_id,
                'entity_type': target_type
            }
        }
        return self.copper.post('/related_links', body)