# Class for cardio subclass of exercise
from exercise import Exercise
from random import randint


class Cardio(Exercise):

    def __init__(self,duration=10, bodyGroup='Total Body', cardioType='Treadmill'):
        print("Cardio class is called")

        super(Cardio, self).__init__(duration, bodyGroup, 2, 'Cardio')

        self.type = cardioType

    def __str__(self):
        return 'Cardio of type : ' + self.type + ' for ' + str(self.duration) + ' minutes.'

    def test(self):
        Exercise.test(self)
        print("Cardio")
        print(self.type)
        


# ex = Cardio(duration = 20, bodyGroup='Arms')
# ex.test()
# ex2 = Cardio(cardioType='Elliptical')
# ex2.test()

