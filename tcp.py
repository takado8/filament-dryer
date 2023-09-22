import network
import socket
from time import sleep
import machine
import utime
from config import load_config

led_onboard = machine.Pin(12, machine.Pin.OUT)
TIMEOUT = 5


class TcpServer:
    def __init__(self):
        _, self.ssid, self.password = load_config()
        ip = self.connect()
        self.connection = self.open_socket(ip)

    def connect(self):
        # Connect to WLAN
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while not wlan.isconnected():
            print('Waiting for connection...')
            sleep(1)

        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        return ip

    def open_socket(self, ip):
        # Open a socket
        address = (ip, 8080)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        connection.settimeout(TIMEOUT)
        print(connection)
        return connection

    def listen(self):
        client = self.connection.accept()[0]
        data = client.recv(1024)
        data = str(data)[2:-1]
        print(data)
        return data
        # resp = handle_response(data)
        # if resp:
        #     client.send(resp.encode())
        # client.close()
