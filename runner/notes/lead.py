from copper_sdk.notes import NoteTarget
import names_generator
import json
import shared_procs

def create_lead_note(copper_client, lead_id, user_id):
    """Create a note for a Lead
    
    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        lead_id (str):
            The Id for the Lead.

    Returns:
        The new note.

    """

    notes = copper_client.notes()
    target = NoteTarget.Lead
    name = names_generator.generate_name(style="capital")
    content = f"{name} greets you from Python"
    return notes.push(target, lead_id, content, user_id)

def get_lead_notes(copper_client, lead_id):
    """Get notes of a Lead.

    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        lead_id (str):
            The Id for the Lead.

    Returns:
        All notes for a Lead.

    """

    notes = copper_client.notes()
    target = NoteTarget.Lead
    return notes.get(target, lead_id)

def run(copper_client, config):
    print("Running Lead Notes examples")
    lead_id = config["LEAD_ID"]
    user_id = int(config["USER_ID"])

    print("Creating note for Lead Id", lead_id)
    new_lead_note = create_lead_note(copper_client, lead_id, user_id)
    print("Note:", json.dumps(new_lead_note))

    shared_procs.wait()

    print("Getting all notes for Lead Id", lead_id)
    lead_notes = get_lead_notes(copper_client, lead_id)
    print(json.dumps(lead_notes))
