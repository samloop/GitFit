#subclass of Environment
from environment import Environment

class Temperature(Environment):

    def __init__(self):
        return

    def getTemp(self, zip):
        e1 = Environment()
        w = e1.getWeather('zip')
        temperature = w.get_temperature('fahrenheit')
        temperature = temperature["temp"]
        return temperature
