from Goal import Goal
from strength import Strength
from cardio import Cardio
from random import randint
from stretch import Stretch

class ImageBasedGoal(Goal):

    def __init__(self):
        super(ImageBasedGoal, self).__init__()
        print("In ImageBasedGoal Class")
        num = input("What intensity level are you feeling today on a scale of 1-3?")
        length = randint(20,30)

        if num == '1':
            self.execution_plan.extend([Stretch(name='Pigeon pose'), Cardio(duration=length, cardioType='Bike'), Strength(exerciseType='Arm Circles'),
                                        Strength(exerciseType='Squats'), Strength(exerciseType='Lunges'),
                                        Strength(exerciseType='Crunches')])
        elif num == '2':
            self.execution_plan.extend([Stretch(name='Pigeon pose'),Cardio(duration=length, cardioType='Elliptical'), Strength(exerciseType='Arm Circles'),
                                        Strength(exerciseType='Squats'), Strength(exerciseType='Lunges'),
                                        Strength(exerciseType='Crunches')])
        elif num == '3':
            self.execution_plan.extend([Stretch(name='Pigeon pose'),Cardio(duration=length, cardioType='Treadmill'), Strength(exerciseType='Arm Circles'),
                                        Strength(exerciseType='Squats'), Strength(exerciseType='Lunges'),
                                        Strength(exerciseType='Crunches')])
        return