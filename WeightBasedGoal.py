from Goal import Goal
from strength import Strength


class WeightBasedGoal(Goal):

    def __init__(self):
        super(WeightBasedGoal, self).__init__()
        bodypart = input("What body part would you like to work: 1 (arms), 2 (legs), 3 (core): ")

        if bodypart == '1':
            self.execution_plan.extend([Strength(exerciseType='Bicep Curls'), Strength(exerciseType='Tricep Pushdown'),
                                        Strength(exerciseType='Shoulder Press'), Strength(exerciseType='Bench Press'),
                                        Strength(exerciseType='Pull ups')])
        elif bodypart == '2':
            self.execution_plan.extend([Strength(exerciseType='Squats'), Strength(exerciseType='Leg Press'),
                                        Strength(exerciseType='Quad Curl'), Strength(exerciseType='Hamstring Curl'),
                                        Strength(exerciseType='Lunges')])

        elif bodypart == '3':
            self.execution_plan.extend([Strength(exerciseType='Plank'), Strength(exerciseType='Russian Twists'),
                                        Strength(exerciseType='Side Bend'), Strength(exerciseType='Crunches'),
                                        Strength(exerciseType='Reverse Crunches')])
        return