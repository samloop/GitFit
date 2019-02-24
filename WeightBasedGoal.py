from Goal import Goal
from cardio import Cardio
from strength import Strength


class WeightBasedGoal(Goal):

    def __init__(self):
        super(WeightBasedGoal, self).__init__()
        self.execution_plan.extend([Strength(bodyGroup='Total Body')])
        return