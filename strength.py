# Class for stregnth subclass of exercise
from exercise import Exercise
from random import randint


class Strength(Exercise):

    def __init__(self,duration=15, bodyGroup='Total Body' , reps=None, sets=None, exerciseType='Free Weight'):

        super(Strength, self).__init__(duration, bodyGroup, 2, 'Strength')
        if reps is None:
            self.reps = randint(6,12)
        else:
            self.reps = reps
        if sets is None:
            self.sets = randint(3,6)
        else:
            self.sets = sets
        self.type = exerciseType

    def __str__(self):
        return 'Strength of type : ' + self.type + ' for ' + str(self.duration) + ' minutes, or ' + str(self.sets) + ' sets with ' + str(self.reps) + ' reps per set.'

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
