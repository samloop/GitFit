from Goal import Goal
from cardio import Cardio
from strength import Strength


class HealthBasedGoal(Goal):

    def __init__(self):
        super(HealthBasedGoal, self).__init__()
        self.execution_plan.extend([Cardio(cardioType='Treadmill'), Strength(exerciseType='Deadlifts')]) # instances of exercises to do
        return