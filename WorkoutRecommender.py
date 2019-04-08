from HealthBasedGoal import HealthBasedGoal
from ImageBasedGoal import ImageBasedGoal
from WeightBasedGoal import WeightBasedGoal
from PerformanceBasedGoal import PerformanceBasedGoal
from LowGoal import LowGoal
from person import Person
from strength import Strength
from exerciseclass import ExerciseClass
from cardio import Cardio
from random import randint

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
        print("Workout 1")
        for ex in self.goal.execution_plan:
            print(ex)

        workoutNum = 2
        while True:
            opinion = input("Was that workout easy(1), ok(2), hard(3) or would you like to quit(4)")

            if opinion == '1':
                for ex in self.goal.execution_plan:
                    if isinstance(ex, Strength):
                        if ex.reps < 10:
                            ex.reps += 2
                        else:
                            ex.sets += 1
                            ex.reps = randint(6,8)
                    elif isinstance(ex, Cardio):
                        ex.duration += 10
                    elif isinstance(ex, ExerciseClass):
                        num = randint(1,3)
                        if num == 1:
                            ex.duration += 15
                        if num == 2:
                            if p1.goal == '1':
                                self.goal = HealthBasedGoal()
                            elif p1.goal == '2':
                                self.goal = ImageBasedGoal()
                            elif p1.goal == '3':
                                self.goal = WeightBasedGoal()
                        else:
                            self.goal = LowGoal()

            #elif opinion == '2':

            #elif opinion =='3':

            else:
                exit()
            print("Workout " + str(workoutNum))
            workoutNum += 1
            for ex in self.goal.execution_plan:
                print(ex)




def main():
    wr = WorkoutRecommender()
    wr.start()




if __name__ == '__main__':
    main()
