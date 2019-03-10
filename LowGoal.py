from Goal import Goal
from exerciseclass import ExerciseClass


class LowGoal(Goal):

    def __init__(self):
        print("In low motivation class")
        super(LowGoal, self).__init__()
        self.execution_plan.extend([ExerciseClass(bodyGroup='Total Body')])
        return