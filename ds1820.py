import machine, onewire, ds18x20, time
from machine import Pin


class DS1820:
    def __init__(self):
        ds_pin = machine.Pin(14, Pin.IN, Pin.PULL_UP)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
        roms = self.ds_sensor.scan()
        self.rom = roms[0]
        print('Found a ds18x20 device')

    def get_temp(self):
        self.ds_sensor.convert_temp()
        return self.ds_sensor.read_temp(self.rom)
