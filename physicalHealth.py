#subclass of health for physio state
from health import Health

class PhysicalHealth(Health):

    def __init__(self):
        super(Health, self).__init__()

    def generateInjury(self):
        self.injury = input("Are you injured? (1) No, (2) Yes: ")
        return self.injury

    def generateSick(self):
        self.sick = input("Are you sick? (1) No, (2) Yes")
        return self.sick
