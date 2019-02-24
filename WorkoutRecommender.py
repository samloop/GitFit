from HealthBasedGoal import HealthBasedGoal
from ImageBasedGoal import ImageBasedGoal
from WeightBasedGoal import WeightBasedGoal
from person import Person
from Goal import Goal


class PerformanceBasedGoal(object):
    pass


class WorkoutRecommender:


    def __init__(self):
        return

    def start(self):
        p1 = Person()
        p1.interview()
        if p1.goal == '1':
            self.goal = HealthBasedGoal()
        elif p1.goal == '2':
            self.goal = ImageBasedGoal()
        elif p1.goal == '3':
            self.goal = PerformanceBasedGoal()
        elif p1.goal == '4':
            self.goal = WeightBasedGoal()


def main():
    wr = WorkoutRecommender()
    wr.start()




if __name__ == '__main__':
    main()
