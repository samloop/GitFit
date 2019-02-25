from Goal import Goal
from strength import Strength
from cardio import Cardio
from random import randint

class ImageBasedGoal(Goal):

    def __init__(self):
        super(ImageBasedGoal, self).__init__()
        num = randint(1,3)

        if num == 1:
            self.execution_plan.extend([Cardio(duration=15, cardioType='Treadmill'), Strength(exerciseType='Bicep Curls'),
                                        Strength(exerciseType='Squats'), Strength(exerciseType='Leg press'),
                                        Strength(exerciseType='Russian Twists')])
        elif num == 2:
            self.execution_plan.extend([Cardio(duration=15, cardioType='Elliptical'), Strength(exerciseType='Bicep Curls'),
                                        Strength(exerciseType='Squats'), Strength(exerciseType='Leg press'),
                                        Strength(exerciseType='Russian Twists')])
        elif num == 3:
            self.execution_plan.extend([Cardio(duration=15, cardioType='Bike'), Strength(exerciseType='Bicep Curls'),
                                        Strength(exerciseType='Squats'), Strength(exerciseType='Leg press'),
                                        Strength(exerciseType='Russian Twists')])
        return