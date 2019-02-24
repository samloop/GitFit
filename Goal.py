class Goal:

    PLANNED = 'Planned'
    STARTED = 'Started'
    COMPLETED = 'Completed'

    def __init__(self):
        self.state = Goal.PLANNED
        self.execution_plan = []
