# Class for exercise


class Exercise:

    def __init__(self, duration=15, bodyGroup='Total Body', intensity=2):
            self.duration = duration
            self.bodyGroup = bodyGroup # We should make a class for this
            self.intensity = intensity

    def test(self):
        print("Exercise")
        print("Duration")
        print(self.duration)
        print("Body Group")
        print(self.bodyGroup)
        print("intensity")
        print(self.intensity)


#ex = Exercise(10, 'Arms')
#ex2 = Exercise()
#ex.test()
#ex2.test()
