from HealthBasedGoal import HealthBasedGoal
from ImageBasedGoal import ImageBasedGoal
from WeightBasedGoal import WeightBasedGoal
from LowGoal import LowGoal
from person import Person
from strength import Strength
from exerciseclass import ExerciseClass
from cardio import Cardio
from environment import Environment
from temperature import Temperature
from altitude import Altitude
from health import Health
from physicalHealth import PhysicalHealth
from mentalHealth import MentalHealth
from random import randint

class WorkoutRecommender:

    def __init__(self):
        return

    def start(self):
        p1 = Person()
        p1.interview()
        ph1 = PhysicalHealth()
        mh1 = MentalHealth()
        injury = ph1.generateInjury()
        t1 = Temperature()
        t1 = t1.getTemp(zip)
        pr1 = Altitude()
        pr1 = pr1.getPressure(zip)
        stress = mh1.generateStress()
        sick = ph1.generateSick()
        strength = False

        if p1.enthusiasm == '1' or p1.experience == '1':
            self.goal = LowGoal()
        elif p1.goal == '1':
            self.goal = HealthBasedGoal()
        elif p1.goal == '2':
            self.goal = ImageBasedGoal()
        elif p1.goal == '3':
            strength = True
            self.goal = WeightBasedGoal()

        # READY TO OUTPUT THE GOAL'S EXECUTION PLAN in nice format
        print("WORKOUT 1")
        for ex in self.goal.execution_plan:
            # environment adjustment
            # temperature
            if t1 >= 80:
                ex.duration -= 3
                print("Because of the heat, your workout was shortened to ", ex.duration, " minutes")
            elif t1 <= 50:
                print("Because of the low temperature of ", t1,
                      " degrees, you should do a 5 minute warm-up jog.")
            else:
                print("Temperature outside is ", t1, ". Enjoy your workout!")

            # altitude
            if pr1 >= 1843:
                if ex.duration >= 15:
                    ex.duration -= 5
                    print("The air is thinner, affecting physical performance. Workout has been "
                          "shortened to ", ex.duration, " minutes")
            else:
                print("Atmospheric pressure of ", pr1, " hPA shouldn't affect workout.")

            # health adjustment
            if injury == '2':
                if strength:
                    print("If you are injured, use low weights or no weights at all "
                          "- use resistance bands and bodyweight instead.")
                else:
                    print("Given your injury, if anything feels hurt during your workout, "
                          "stop what you're doing and RICE it.")
            if sick == '2':
                print("If you feel sick with above the neck, you can workout as usual, just monitor "
                      "how you feel. If you feel sick below the neck, take today as a rest day!")
            if (stress == '2') | (stress == '3'):
                if strength:
                    print(
                        "Consider doing a superset so your workout takes less time (no rest between exercises.)")
                else:
                    if ex.duration >= 15:
                        ex.duration -= 5
                        print("Workout shortened to account for stress.")
            print(ex)

        workoutNum = 2
        while True:
            opinion = input("Was that workout easy(1), ok(2), hard(3) or would you like to quit(4)")
            if int(opinion) > 3:
                exit()
            adjust = input("Do you want to adjust the current plan(1) or create a new one(2)?")

            if adjust == '1':
                if opinion == '1':
                    print("The workout will be harder by increasing reps/sets")
                    for ex in self.goal.execution_plan:
                        if isinstance(ex, Strength):
                            if ex.reps < 10:
                                ex.reps += 2
                            else:
                                ex.sets += 1
                                ex.reps = randint(6,8)
                        elif isinstance(ex, Cardio):
                            if ex.type == 'Treadmill':
                                ex.duration += 10
                            else:
                                ex.type = 'Treadmill'
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
                elif opinion == '2':
                    print("The workout will be similar by slightly increasing reps/sets")
                    for ex in self.goal.execution_plan:
                        if isinstance(ex, Strength):
                            if ex.reps < 12:
                                ex.reps += 1
                            else:
                                ex.sets += 1
                                ex.reps = randint(6,8)
                        elif isinstance(ex, Cardio):
                            ex.duration += 5
                elif opinion == '3':
                    print("The workout will be easier by slightly decreasing reps/sets")
                    for ex in self.goal.execution_plan:
                        if isinstance(ex, Strength):
                            if ex.reps > 6:
                                ex.reps -= 1
                            else:
                                ex.sets -= 1
                                ex.reps = randint(8,12)
                        elif isinstance(ex, Cardio):
                            ex.duration -= 10
                        elif isinstance(ex, ExerciseClass):
                            num = randint(1,2)
                            if num == 1:
                                ex.duration -= 15
                            else:
                                self.goal = LowGoal()

            elif adjust == '2':
                print("A new workout will be made")
                p1.interview()
                if p1.enthusiasm == '1' or p1.experience == '1':
                    self.goal = LowGoal()
                elif p1.goal == '1':
                    self.goal = HealthBasedGoal()
                elif p1.goal == '2':
                    self.goal = ImageBasedGoal()
                elif p1.goal == '3':
                    self.goal = WeightBasedGoal()

            print("WORKOUT " + str(workoutNum))
            workoutNum += 1
            for ex in self.goal.execution_plan:
                print(ex)


def main():
    wr = WorkoutRecommender()
    wr.start()




if __name__ == '__main__':
    main()
