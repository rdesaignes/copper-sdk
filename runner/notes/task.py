from copper_sdk.notes import NoteTarget
import names_generator
import json
import shared_procs

def create_task_note(copper_client, task_id):
    """Create a note for a Task
    
    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        task_id (str):
            The Id for the Task.

    Returns:
        The new note.

    """

    notes = copper_client.notes()
    target = NoteTarget.Task
    name = names_generator.generate_name(style="capital")
    content = f"{name} greets you from Python"
    return notes.push(target, task_id, content)

def get_task_notes(copper_client, task_id):
    """Get notes of a Task.

    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        task_id (str):
            The Id for the Task.

    Returns:
        All notes for a Task.

    """

    notes = copper_client.notes()
    target = NoteTarget.Task
    return notes.get(target, task_id)


def run(copper_client, config):
    print("Running Task Notes examples")
    task_id = config["TASK_ID"]

    print("Creating note for Task Id", task_id)
    new_task_note = create_task_note(copper_client, task_id)
    print("Note:", json.dumps(new_task_note))

    shared_procs.wait()

    print("Getting all notes for Task Id", task_id)
    task_notes = get_task_notes(copper_client, task_id)
    print(json.dumps(task_notes))


def create_task_note_old(copper_client, task_id):
    """Create a note for a Task (old method)
    
    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        task_id (str):
            The Id for the Task.

    Returns:
        The new note.

    """

    return copper_client.tasks().pull_notes(task_id)

def get_task_notes_old(copper_client, task_id):
    """Get notes of a Task (old method).

    Attributes:
        copper_client (copper_sdk.copper):
            The CopperSDK client.
        task_id (str):
            The Id for the Task.

    Returns:
        All notes for a Task.

    """
    name = names_generator.generate_name(style="capital")
    content = f"{name} greets you from Python"
    return copper_client.tasks().push_note(task_id, content)

def run_old(copper_client, config):
    """Old example on upload and download task notes.
    
    This uses the notes fns of `copper_sdk.Task`.

    """

    print("Old example on pushing Task Notes")
    task_id = config["TASK_ID"]

    print("Creating note for Task Id", task_id)
    new_task_note = create_task_note_old(copper_client, task_id)
    print("Note:", json.dumps(new_task_note))

    shared_procs.wait()

    print("Getting all notes for Task Id", task_id)
    task_notes = get_task_notes_old(copper_client, task_id)
    print(json.dumps(task_notes))
