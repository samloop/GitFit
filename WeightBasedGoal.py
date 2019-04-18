from Goal import Goal
from strength import Strength
from stretch import Stretch
from random import randint


class WeightBasedGoal(Goal):

    def __init__(self):
        super(WeightBasedGoal, self).__init__()
        print("In WeightBasedGoal Class")

        bodypart = input("What body part would you like to work: 1 (arms), 2 (legs), 3 (core): ")
        num = randint(1,4)

        if bodypart == '1':
            if num == 1:
                self.execution_plan.extend([Stretch(name='Arm circles'), Strength(exerciseType='Reverse Curls'),
                                            Strength(exerciseType='Pushup'),
                                            Strength(exerciseType='Shoulder Press'),
                                            Strength(exerciseType='Tricep Dips'),
                                            Strength(exerciseType='Pull ups')])
            elif num == 2:
                self.execution_plan.extend([Stretch(name='Arm circles'), Strength(exerciseType='Bicep Curls'),
                                            Strength(exerciseType='Tricep Pushdown'),
                                            Strength(exerciseType='Shoulder Press'),
                                            Strength(exerciseType='Bench Press'),
                                            Strength(exerciseType='Pull ups')])
            elif num == 3:
                self.execution_plan.extend([Stretch(name='Side plank'), Strength(exerciseType='Hammer Curls'),
                                            Strength(exerciseType='Tricep Extensions'),
                                            Strength(exerciseType='Front Arm Raises'),
                                            Strength(exerciseType='Bench Press'),
                                            Strength(exerciseType='Pull ups')])
            elif num == 4:
                self.execution_plan.extend([Stretch(name='Side plank'), Strength(exerciseType='Bicep Curls'),
                                            Strength(exerciseType='Side Arm Raises'),
                                            Strength(exerciseType='Shoulder Press'),
                                            Strength(exerciseType='Bench Press'),
                                            Strength(exerciseType='Hammer Curls')])
        elif bodypart == '2':
            if num == 1:
                self.execution_plan.extend([Stretch(name='Butterfly'), Strength(exerciseType='Deadlift'),
                                            Strength(exerciseType='Pistol Squat'),
                                            Strength(exerciseType='Quad Curl'), Strength(exerciseType='Hamstring Curl'),
                                            Strength(exerciseType='Lunges')])
            elif num == 2:
                self.execution_plan.extend([Stretch(name='Butterfly'), Strength(exerciseType='Squats'),
                                            Strength(exerciseType='Leg Press'),
                                            Strength(exerciseType='Quad Curl'), Strength(exerciseType='Downward Leg Lift'),
                                            Strength(exerciseType='Calf Raises')])
            elif num == 3:
                self.execution_plan.extend([Stretch(name='Seated toe touches'), Strength(exerciseType='Squats'),
                                            Strength(exerciseType='Leg Press'),
                                            Strength(exerciseType='Quad Curl'), Strength(exerciseType='Clam Shells'),
                                            Strength(exerciseType='Lateral Lunges')])
            elif num == 4:
                self.execution_plan.extend([Stretch(name='Seated toe touches'), Strength(exerciseType='Deadlift'),
                                            Strength(exerciseType='Leg Press'),
                                            Strength(exerciseType='Squats'), Strength(exerciseType='Hamstring Curl'),
                                            Strength(exerciseType='Lunges')])

        elif bodypart == '3':
            if num == 1:
                self.execution_plan.extend([Stretch(name='Downward dog'), Strength(exerciseType='Plank'),
                                            Strength(exerciseType='Russian Twists'),
                                            Strength(exerciseType='Side Bend'), Strength(exerciseType='Crunches'),
                                            Strength(exerciseType='Reverse Crunches')])
            elif num == 2:
                self.execution_plan.extend([Stretch(name='Downward dog'), Strength(exerciseType='Star Plank'),
                                            Strength(exerciseType='Flutter Kicks'),
                                            Strength(exerciseType='Side Bend'), Strength(exerciseType='Knee Crunches'),
                                            Strength(exerciseType='Reverse Crunches')])
            elif num == 3:
                self.execution_plan.extend([Stretch(name='Forward Bend'), Strength(exerciseType='Plank'),
                                            Strength(exerciseType='Flutter Kicks'),
                                            Strength(exerciseType='Toe Touches'), Strength(exerciseType='Knee es'),
                                            Strength(exerciseType='Bicycle Crunches')])
            elif num == 4:
                self.execution_plan.extend([Stretch(name='Forward Bend'), Strength(exerciseType='Star Plank'),
                                            Strength(exerciseType='Russian Twists'),
                                            Strength(exerciseType='Side Bend'), Strength(exerciseType='Crunches'),
                                            Strength(exerciseType='Bicycle Crunches')])
        return