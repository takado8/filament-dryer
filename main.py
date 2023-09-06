from peltier import Peltier
from ds1820 import DS1820
from time import sleep, time
from fans import Fans
from dht11 import get_temp_and_humidity, get_dew_point
from thingspeak import send_data


COLD_MODE_DURATION = 60 * 10
AVERAGE_LEN = 10
SLEEP_TIME = 6
OFF = 'OFF'
ON = 'ON'
REVERSED = 'REVERSED'
REVERSED_MIN_TEMP = 16
REVERSED_MAX_TEMP = 45
NORMAL_MAX_TEMP = 40

peltier = Peltier()
ds = DS1820()
fans = Fans()


def run():
    mode = OFF
    next_mode = ON

    mode_start_time = 0
    aggregate_temp = []
    aggregate_temp_in = []
    aggregate_humidity = []
    aggregate_dew_point = []

    while True:
        temp = ds.get_temp()
        time_left = COLD_MODE_DURATION - round(time() - mode_start_time)
        t, h = get_temp_and_humidity()
        dew_point = get_dew_point(t, h)
        aggregate_temp.append(temp)
        aggregate_temp_in.append(t)
        aggregate_humidity.append(h)
        aggregate_dew_point.append(dew_point)
        if len(aggregate_temp) == AVERAGE_LEN:
            avg_temp = sum(aggregate_temp) / AVERAGE_LEN
            avg_temp_in = sum(aggregate_temp_in) / AVERAGE_LEN
            avg_humidity = sum(aggregate_humidity) / AVERAGE_LEN
            avg_dew_point = sum(aggregate_dew_point) / AVERAGE_LEN
            print(f'\navg_t: {avg_temp}\navg_t_in: {avg_temp_in}\navg_hum: {avg_humidity}\navg_dew: {avg_dew_point}')
            send_data(avg_temp_in, avg_temp, avg_humidity, avg_dew_point)
            aggregate_temp.clear()
            aggregate_temp_in.clear()
            aggregate_humidity.clear()
            aggregate_dew_point.clear()
        print(f'\n\ntemp in: {t}*C\nhumidity: {h}%\ndew point: {int(dew_point)}*C')
        print(f'\ntemp: {temp}*C')
        # print(f'mode: {mode}\nnext mode: {next_mode}')
        # if mode == ON and time_left <= 0:
        #     print('Switching to neutral state 1')
        #     peltier.turn_off_peltier()
        #     fans.turn_off_fan1()
        #     mode = OFF
        #     next_mode = REVERSED
        # elif mode == ON and time_left > 0:
        #     print(f'time left: {time_left}')
        # elif mode == OFF and next_mode == REVERSED and temp >= REVERSED_MIN_TEMP:
        #     print('Switching to reversed state.')
        #     fans.turn_on_fan2()
        #     sleep(1)
        #     peltier.turn_on_peltier_reversed()
        #     mode = REVERSED
        #     next_mode = OFF
        #
        # elif mode == REVERSED and temp >= REVERSED_MAX_TEMP:
        #     print('Switching to neutral state 2')
        #     peltier.turn_off_peltier()
        #     mode = OFF
        #     next_mode = ON
        #
        # elif mode == OFF and next_mode == ON and temp <= NORMAL_MAX_TEMP:
        #     print('Switching on.')
        #     fans.turn_off_fan2()
        #     fans.turn_on_fan1()
        #     peltier.turn_on_peltier_normal()
        #     mode = ON
        #     next_mode = OFF
        #     mode_start_time = time()

        sleep(SLEEP_TIME)
