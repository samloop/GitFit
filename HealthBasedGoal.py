from Goal import Goal
from cardio import Cardio
from strength import Strength
from random import randint


class HealthBasedGoal(Goal):

    def __init__(self):
        super(HealthBasedGoal, self).__init__()
        num = randint(1,3)
        if num == 1:
            self.execution_plan.extend([Cardio(cardioType='Treadmill'), Strength(exerciseType='Deadlifts')]) # instances of exercises to do
        elif num == 2:
            self.execution_plan.extend([Cardio(cardioType='Elliptical'), Strength(exerciseType='Free weights')])
        elif num == 3:
            self.execution_plan.extend([Cardio(cardioType='Bike'), Strength(exerciseType='Bicep Curls')])
        return