# Class for cardio subclass of exercise
from exercise import Exercise
from random import randint


class Cardio(Exercise):

    def __init__(self,duration=10, bodyGroup='Total Body', cardioType='Treadmill'):

        Exercise.__init__(self, duration, bodyGroup)
        self.type = cardioType

    def test(self):
        Exercise.test(self)
        print("Cardio")
        print(self.type)
        


# ex = Cardio(duration = 20, bodyGroup='Arms')
# ex.test()
# ex2 = Cardio(cardioType='Elliptical')
# ex2.test()

