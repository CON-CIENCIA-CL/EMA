from setups import SDL_Pi_HDC1080
import sys
import os

# Setting main path to HDC1080
sys.path.append('./setups/SDL_Pi_HDC1080')
hdc1080 = SDL_Pi_HDC1080()

# Getting temperature
def HDCtemp(roundto):
	temperature = round(hdc1080.readTemperature(), roundto)
	return temperature

# Getting humidity
def HDChum(roundto):
	humidity = round(hdc1080.readHumidity(), roundto)
	return humidity

print(HDChum(2))
print(HDCtemp(2))
