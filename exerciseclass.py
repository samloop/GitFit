# Class for exercise class subclass of exercise
from exercise import Exercise
from random import randint


class ExerciseClass(Exercise):

    def __init__(self,duration=60, bodyGroup='Total Body', instructor='Unknown'):

        super(ExerciseClass, self).__init__(duration, bodyGroup, instructor)
        self.instructor = instructor
        num = randint(1,4)
        if num == 1:
            self.type = 'Spin Class'
        elif num == 2:
            self.type = 'Zumba Class'
        elif num == 3:
            self.type = 'Yoga Class'
        elif num == 4:
            self.type = 'HIIT Class (ex. Orange Theory'

    def __str__(self):
        return 'Exercise class of type : ' + self.type + ' for : ' + self.bodyGroup + ' for ' + str(self.duration) + ' minutes'

    def test(self):
        Exercise.test(self)
        print("Exercise Class")
        print(self.instructor)
        print(self.type)
        


# ex = ExerciseClass(duration = 20, bodyGroup='Arms')
# ex.test()
# ex2 = ExerciseClass(instructor='Jessica Hayes', classType='KickBoxing')
# ex2.test()

