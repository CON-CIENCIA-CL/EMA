import sys
from components.setups import SDL_Pi_HDC1080

class HDC:
    def __init__(self):
        sys.path.append('./modules/SDL_Pi_HDC1080_Python3')
        self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

    def temp(self):
        temperature = self.hdc1080.readTemperature()
        return temperature

    def hum(self):
        humidity = self.hdc1080.readHumidity()
        return humidity
        
    def read(self, decimal):
        temp = self.temp(decimal)
        hum = self.hum(decimal)
        return temp, hum

HDC = HDC()

temperature, humidity = HDC.read(decimal=2)

print(f'temp: {temperature}; hum: {humidity}')