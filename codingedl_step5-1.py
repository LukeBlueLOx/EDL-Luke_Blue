from components import LightSensor
from time import sleep, time

light = LightSensor("D6")
while True:
    lightlevel = (light.reading)
    print lightlevel