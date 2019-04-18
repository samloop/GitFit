#Class for environment
import pyowm

owm = pyowm.OWM('86ae4a8106ec337ece9c29f768886734')

class Environment:

    def __init__(self):
        return

    def getWeather(self, zip):
        observation = owm.weather_at_place('zip')
        w = observation.get_weather()
        return w
