from Goal import Goal
from cardio import Cardio
from stretch import Stretch


class HealthBasedGoal(Goal):

    def __init__(self):
        super(HealthBasedGoal, self).__init__()
        print("In HealthBasedGoal Class")

        num = input("What intensity level are you feeling today on a scale of 1-3?")

        if num == 1:
            self.execution_plan.extend([Stretch(name='Lunges'), Cardio(duration=25, cardioType='Bike')]) # instances of exercises to do
        elif num == 2:
            self.execution_plan.extend([Stretch(name='Crossack squat'), Cardio(duration=30, cardioType='Elliptical')])
        elif num == 3:
            self.execution_plan.extend([Stretch(name='Calf raises'), Cardio(duration=35, cardioType='Treadmill')])

        return