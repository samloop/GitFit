#subclass of environment
from environment import Environment

class Altitude(Environment):

    def __init__(self):
        return

    def getPressure(self, zip):
        e1 = Environment()
        w = e1.getWeather('zip')
        pressure = w.get_pressure()
        return pressure["press"]
