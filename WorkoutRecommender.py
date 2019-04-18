from HealthBasedGoal import HealthBasedGoal
from ImageBasedGoal import ImageBasedGoal
from WeightBasedGoal import WeightBasedGoal
from PerformanceBasedGoal import PerformanceBasedGoal
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
        print("Workout 1")
        for ex in self.goal.execution_plan:
            print(ex)

        workoutNum = 2
        while True:
            opinion = input("Was that workout easy(1), ok(2), hard(3) or would you like to quit(4)")
            if int(opinion) > 3:
                exit()
            adjust = input("Do you want to adjust the current plan(1) or create a new one(2)?")

            if adjust == '1':
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

            elif adjust == '2':
                p1.interview()
                if p1.enthusiasm == '1' or p1.experience == '1':
                    self.goal = LowGoal()
                elif p1.goal == '1':
                    self.goal = HealthBasedGoal()
                elif p1.goal == '2':
                    self.goal = ImageBasedGoal()
                elif p1.goal == '3':
                    self.goal = WeightBasedGoal()

                    # environment adjustment
                    # temperature
                    t1 = Temperature()
                    t1 = t1.getTemp(zip)
                    if t1 >= 80:
                        ex.duration -= 5
                        print("Because of the heat, your workout was shortened to ", ex.duration, " minutes")
                    elif t1 <= 50:
                        print("Because of the low temperature of ", t1,
                              " degrees, you should do a 5 minute warm-up jog.")
                    else:
                        print("Temperature outside is ", t1, ". Enjoy your workout!")

            # altitude
            p1 = Altitude()
            p1 = p1.getPressure(zip)
            if p1 >= 1843:
                if ex.duration >= 15:
                    ex.duration -= 5
                    print("The air is thinner, affecting physical performance. Workout has been "
                          "shortened to ", ex.duration, " minutes")
            else:
                print("Atmospheric pressure of ", p1, " hPA shouldn't affect workout.")

            # health adjustment
            ph1 = PhysicalHealth()
            mh1 = MentalHealth()
            if ph1.generateInjury() == 2:
                if strength:
                    print("If you are injured, use low weights or no weights at all "
                          "- use resistance bands and bodyweight instead.")
                else:
                    print("Given your injury, if anything feels hurt during your workout, "
                          "stop what you're doing and RICE it.")
            if ph1.generateSick() == 2:
                print("If you feel sick with above the neck, you can workout as usual, just monitor "
                      "how you feel. If you feel sick below the neck, take today as a rest day!")
            stress = mh1.generateStress()
            if (stress == 2) | (stress == 3):
                if strength:
                    print(
                        "Consider doing a superset so your workout takes less time (no rest between exercises.)")
                else:
                    if ex.duration >= 15:
                        ex.duration -= 5
                        print("Workout shortened for the sake of time.")

            print("Workout " + str(workoutNum))
            workoutNum += 1
            for ex in self.goal.execution_plan:
                print(ex)




def main():
    wr = WorkoutRecommender()
    wr.start()




if __name__ == '__main__':
    main()
