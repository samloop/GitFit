# Class for stregnth subclass of exercise
from exercise import Exercise
from random import randint


class Strength(Exercise):

    def __init__(self,duration=None, bodyGroup=None , reps=None, sets=None, type=None):
        Exercise.__init__(self, duration, bodyGroup)
        if reps is None:
            self.reps = randint(6,12)
        else:
            self.reps = reps
        if sets is None:
            self.sets = randint(3,6)
        else:
            self.sets = sets
        if type is None:
            self.type = 'Free Weight'
        else:
            self.type = type

    def test(self):
        Exercise.test(self)
        print("Strength")
        print("Reps")
        print(self.reps)
        print("Sets")
        print(self.sets)
        print("Type")
        print(self.type)


#ex = Strength(duration = 20, bodyGroup='Arms',reps = 15, sets = 3, type = 'Machine')
#ex.test()
#ex2 = Strength(reps = 15, sets = 3, type = 'Machine')
#ex2.test()
#ex3 = Strength()
#ex3.test()
