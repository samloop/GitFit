# Class for exercise class subclass of exercise
from exercise import Exercise
from random import randint


class ExerciseClass(Exercise):

    def __init__(self,duration=10, bodyGroup='Total Body', instructor='Unknown', classType='Spin Class'):

        super(ExerciseClass, self).__init__(duration, bodyGroup, instructor, 'Aerobic Dance Class')
        self.instructor = instructor
        self.type = classType


    def test(self):
        Exercise.test(self)
        print("Exercise Class")
        print(self.instructor)
        print(self.type)
        


# ex = ExerciseClass(duration = 20, bodyGroup='Arms')
# ex.test()
# ex2 = ExerciseClass(instructor='Jessica Hayes', classType='KickBoxing')
# ex2.test()

