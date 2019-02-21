# Class for cardio subclass of exercise
from exercise import Exercise
from random import randint


class Stretch(Exercise):

    def __init__(self,duration=10, bodyGroup='Total Body'):

        Exercise.__init__(self, duration, bodyGroup)

    def test(self):
        Exercise.test(self)
        print("Stretch")
        


# ex = Stretch(duration = 20, bodyGroup='Arms')
# ex.test()
# ex2 = Stretch()
# ex2.test()

