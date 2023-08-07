from copper_sdk import copper
from dotenv import dotenv_values
import notes.lead
import notes.opportunity
import notes.task

def notes_examples(copper_client, config):
    notes.lead.run(copper_client, config)
    notes.opportunity.run(copper_client, config)
    notes.task.run(copper_client, config)
    # notes.task.run_old(copper_client, config)

if __name__ == "__main__":
    config = dotenv_values(".env")
    copper_client = copper.Copper(config["TOKEN"], config["EMAIL"])
    notes_examples(copper_client, config)
