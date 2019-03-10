from HealthBasedGoal import HealthBasedGoal
from ImageBasedGoal import ImageBasedGoal
from WeightBasedGoal import WeightBasedGoal
from PerformanceBasedGoal import PerformanceBasedGoal
from LowGoal import LowGoal
from person import Person

class WorkoutRecommender:


    def __init__(self):
        return

    def start(self):
        p1 = Person()
        p1.interview()

        if p1.enthusiasm == '1' or p1.experience == '1':
            self.goal = LowGoal()
        elif p1.goal == '1':
            self.goal = HealthBasedGoal()
        elif p1.goal == '2':
            self.goal = ImageBasedGoal()
        elif p1.goal == '3':
            self.goal = WeightBasedGoal()

        # READY TO OUTPUT THE GOAL'S EXECUTION PLAN in nice format
        for ex in self.goal.execution_plan:
            print(ex)


def main():
    wr = WorkoutRecommender()
    wr.start()




if __name__ == '__main__':
    main()
