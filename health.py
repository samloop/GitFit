#Class for health/physio state

class Health:

    NEEDSCHECK = 'Needs Check'
    CHECKED = 'Checked'

    def __init__(self):
        self.state = Health.NEEDSCHECK
        print("Checking health now...")
        return
