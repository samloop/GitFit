# Class for exercise


class Exercise:

    def __init__(self, duration=None, bodyGroup=None):
        if duration is None:
            self.duration = 15
        else:
            self.duration = duration
        if bodyGroup is None:
            self.bodyGroup = 'Total Body'  #We should create a class for the different body group
        else:
            self.bodyGroup = bodyGroup

    def test(self):
        print("Exercise")
        print("Duration")
        print(self.duration)
        print("Body Group")
        print(self.bodyGroup)


#ex = Exercise(10, 'Arms')
#ex2 = Exercise()
#ex.test()
#ex2.test()
