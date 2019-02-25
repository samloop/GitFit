from Goal import Goal
from strength import Strength
from cardio import Cardio
from random import randint


class PerformanceBasedGoal(Goal):

    def __init__(self):
        super(PerformanceBasedGoal, self).__init__()
        num = randint(1,3)
        if num == 1:
            self.execution_plan.extend([Strength(exerciseType='Bicep Curls'), Strength(exerciseType='Squats'),
                                        Strength(exerciseType='Shoulder Press'), Strength(exerciseType='Hamstring Curl'),
                                        Cardio(cardioType='Treadmill')])
        elif num == 2:
            self.execution_plan.extend([Strength(exerciseType='Squats'), Strength(exerciseType='Plank'),
                                        Strength(exerciseType='Bench Press'), Strength(exerciseType='Hamstring Curl'),
                                        Cardio(cardioType='Treadmill')])

        elif num == 3:
            self.execution_plan.extend([Strength(exerciseType='Tricep pushdown'), Strength(exerciseType='Russian Twists'),
                                        Strength(exerciseType='Push Ups'), Strength(exerciseType='Crunches'),
                                        Cardio(cardioType='Treadmill')])

        return