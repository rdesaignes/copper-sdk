import time

def wait():
    """Wait 7 seconds.

    CopperCRM need some seconds to reflect changes in UI and in REST API.

    """

    print()
    print("Waiting 7 secs...")
    time.sleep(7)
    print()
    print()