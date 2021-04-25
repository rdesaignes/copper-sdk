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

    def push(self, target: NoteTarget, target_id, content, user_id = 0):
        """Send notes into an NoteTarget entity"""

        parent = {
            "type": target.to_str(),
            "id": target_id
        }

        # Fixed value from Copper for notes.
        req_type = {
            "category": "user",
            "id": 0
        }

        body = {
            "parent": parent,
            "type": req_type,
            "details": content
        }

        if isinstance(user_id, int):
            if user_id > 0:
                body["user_id"] = user_id

        return self.copper.activities().create(body)

    def get(self, target: NoteTarget, target_id, user_id = 0):
        """Request notes from an NoteTarget entity"""

        parent = {
            "type": target.to_str(),
            "id": target_id
        }

        body = {
            "parent": parent
        }

        return self.copper.activities().list(body)
