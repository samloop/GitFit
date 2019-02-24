from Goal import Goal
from strength import Strength
from random import randint

class ImageBasedGoal(Goal):

    def __init__(self):
        super(ImageBasedGoal, self).__init__()
        self.execution_plan.extend([Strength(exerciseType='Bicep Curls'), Strength(exerciseType='Squats'),
                                    Strength(exerciseType='Leg press'), Strength(exerciseType='Russian Twists')])
        return