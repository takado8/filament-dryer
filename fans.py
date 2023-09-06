from machine import Pin
import machine


class Fans:
    def __init__(self):
        self.fan1 = machine.Pin(12, Pin.OUT, value=1)
        self.fan2 = machine.Pin(13, Pin.OUT, value=1)

    def turn_on_fan1(self):
        self.fan1.value(0)

    def turn_on_fan2(self):
        self.fan2.value(0)

    def turn_off_fan1(self):
        self.fan1.value(1)

    def turn_off_fan2(self):
        self.fan2.value(1)
