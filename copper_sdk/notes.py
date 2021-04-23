from enum import Enum

class NoteTarget(Enum):
    """For which target is the note for"""
    Task = "task"
    Opportunity = "opportunity"
    Lead = "lead"

    def to_str(self):
        return self.value

class Notes:
    def __init__(self, copper):
        self.copper = copper

    def push(self, target: NoteTarget, target_id, content):
        """Send notes to a task"""

        parent = {
            "type": target.to_str(),
            "id": target_id
        }

        # Fixed value from Copper for tasks.
        req_type = {
            "category": "user",
            "id": 0
        }

        body = {
            "parent": parent,
            "type": req_type,
            "details": content
        }

        return self.copper.activities().create(body)

    def get(self, target: NoteTarget, target_id):
        """Request notes from a task"""

        task_parent = {
            "type": target.to_str(),
            "id": target_id
        }

        body = {
            "parent": task_parent
        }

        return self.copper.activities().list(body)
