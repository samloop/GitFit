from HealthBasedGoal import HealthBasedGoal
from ImageBasedGoal import ImageBasedGoal
from WeightBasedGoal import WeightBasedGoal
from PerformanceBasedGoal import PerformanceBasedGoal
from exerciseclass import ExerciseClass
from person import Person
from Goal import Goal


class WorkoutRecommender:


    def __init__(self):
        return

    def start(self):
        p1 = Person()
        p1.interview()

        if p1.goal == '1':
            self.goal = HealthBasedGoal()
        elif p1.goal == '1' and p1.enthusiasm == '1':
            self.goal = HealthBasedGoal()
        elif p1.goal == '2':
            self.goal = ImageBasedGoal()
        elif p1.goal == '3':
            self.goal = PerformanceBasedGoal()
        elif p1.goal == '4':
            self.goal = WeightBasedGoal()

        # READY TO OUTPUT THE GOAL'S EXECUTION PLAN in nice format
        for ex in self.goal.execution_plan:
            print(ex)


def main():
    wr = WorkoutRecommender()
    wr.start()




if __name__ == '__main__':
    main()
