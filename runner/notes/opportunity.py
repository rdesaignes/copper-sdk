from copper_sdk.notes import NoteTarget
import names_generator
import json
import shared_procs

def create_opportunity_note(copper_client, opportunity_id, user_id):
    """Create a note for a Opportunity
    
    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        opportunity_id (str):
            The Id for the Opportunity.

    Returns:
        The new note.

    """

    notes = copper_client.notes()
    target = NoteTarget.Opportunity
    name = names_generator.generate_name(style="capital")
    content = f"{name} greets you from Python"
    return notes.push(target, opportunity_id, content, user_id)

def get_opportunity_notes(copper_client, opportunity_id):
    """Get notes of a Opportunity.

    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        opportunity_id (str):
            The Id for the Opportunity.

    Returns:
        All notes for a Opportunity.

    """

    notes = copper_client.notes()
    target = NoteTarget.Opportunity
    return notes.get(target, opportunity_id)


def run(copper_client, config):
    print("Running Opportunity Notes examples")
    opportunity_id = config["OPPORTUNITY_ID"]
    user_id = int(config["USER_ID"])

    print("Creating note for Opportunity Id", opportunity_id)
    new_opportunity_note = create_opportunity_note(copper_client, opportunity_id, user_id)
    print("Note:", json.dumps(new_opportunity_note))

    shared_procs.wait()

    print("Getting all notes for Opportunity Id", opportunity_id)
    opportunity_notes = get_opportunity_notes(copper_client, opportunity_id)
    print(json.dumps(opportunity_notes))
