from Goal import Goal
from cardio import Cardio
from strength import Strength


class HealthBasedGoal(Goal):

    def __init__(self):

        self.execution_plan.extend([Cardio, Strength]) # instances of exercises to do
        return