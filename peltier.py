from machine import Pin
import machine


class Peltier:
    def __init__(self):
        self.ch1 = machine.Pin(5, Pin.OUT, value=1)
        self.ch2 = machine.Pin(4, Pin.OUT, value=1)
        self.ch3 = machine.Pin(0, Pin.OUT, value=1)
        self.ch4 = machine.Pin(2, Pin.OUT, value=1)
        self.all_channels = [self.ch1, self.ch2, self.ch3, self.ch4]

    def turn_on_peltier_normal(self):
        self.ch1.value(0)
        self.ch4.value(0)

    def turn_on_peltier_reversed(self):
        self.ch2.value(0)
        self.ch3.value(0)

    def turn_off_peltier(self):
        for ch in self.all_channels:
            ch.value(1)
