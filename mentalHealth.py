#subclass of health for mental health
from health import Health

class MentalHealth(Health):

    def __init__(self):
        super(Health, self).__init__()

    def generateStress(self):
        stress = input("How stressed would you say you are? (1) None/a little, (2) Moderately, (3) Extremely: ")
        return stress
