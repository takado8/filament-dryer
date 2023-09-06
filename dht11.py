import dht
from machine import Pin
import math


sensor = dht.DHT11(Pin(16))


def get_temp_and_humidity():
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    return t, h


def get_dew_point(temperature, relative_humidity):
    a = 17.27
    b = 237.7
    alpha = ((a * temperature) / (b + temperature)) + math.log(relative_humidity / 100.0)
    dew = (b * alpha) / (a - alpha)
    return dew
