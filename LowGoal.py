from Goal import Goal
from exerciseclass import ExerciseClass


class LowGoal(Goal):

    def __init__(self):
        super(LowGoal, self).__init__()
        self.execution_plan.extend([ExerciseClass(bodyGroup='Total Body')])
        return