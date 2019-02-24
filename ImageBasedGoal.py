from Goal import Goal
from strength import Strength

class ImageBasedGoal(Goal):

    def __init__(self):
        super(ImageBasedGoal, self).__init__()
        self.execution_plan.extend([Strength()]) # instances of exercises to do
        return