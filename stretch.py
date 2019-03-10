# Class for stretch subclass of exercise
from exercise import Exercise
from random import randint


class Stretch(Exercise):

    def __init__(self,duration=10, bodyGroup='Total Body', name='downward dog'):
        print("Stretch class is called")

        super(Stretch, self).__init__(duration, bodyGroup, name)
        self.name = name

    def __str__(self):
        return 'Stretch of type : ' + self.name

    def test(self):
        Exercise.test(self)
        print("Stretch")
        


# ex = Stretch(duration = 20, bodyGroup='Arms')
# ex.test()
# ex2 = Stretch()
# ex2.test()

