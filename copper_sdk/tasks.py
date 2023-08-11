from copper_sdk.base import BaseResource
from copper_sdk.notes import NoteTarget


class Tasks(BaseResource):
    
    def __init__(self, copper):
        self.copper = copper

    def get(self, id):
        return self.copper.get('/tasks/' + id)

    def create(self, body = {}):
        return self.copper.post('/tasks', body)

    def update(self, id, body = {}):
        return self.copper.put('/tasks/' + id, body)

    def delete(self, id):
        return self.copper.delete('/tasks/' + id)   

    def list(self, body = {}):
        default_body = {
            'page_number': 1,  # number	The page number (starting with 1) that you would like to view.
            'page_size': 20,  # number	The number of entries included in a page of results
            'sort_by': 'name',  # string	The field on which to sort the results (see footnote 1).
            'sort_direction': 'asc',  # string	The direction in which to sort the results. Possible values are: asc or desc.
        }
        return self.copper.post('/tasks/search', { **default_body, **body})

    def push_note(self, task_id, content):
        """Push a note into a task"""
        target = NoteTarget.Task
        return self.copper.notes().push(target, task_id, content)

    def pull_notes(self, task_id):
        """Request notes from a task"""
        target = NoteTarget.Task
        return self.copper.notes().get(target, task_id)
