import network
import urequests
import ujson
from time import sleep
from config import load_config


api_key, ssid, password = load_config()

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

# Wait for the Wi-Fi connection to be established
while not wifi.isconnected():
    print('Waiting for connection...')
    sleep(1)

ip = wifi.ifconfig()[0]
print(f'Connected on {ip}')


def send_data(value1, value2, value3, value4):
    data = {
        "api_key": api_key,
        "field1": value1,
        "field2": value2,
        "field3": value3,
        "field4": value4
    }
    json_data = ujson.dumps(data)
    url = 'https://api.thingspeak.com/update.json'
    try:
        response = urequests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print("Data sent successfully to Thingspeak.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
        response.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
