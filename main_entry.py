from tcp import TcpServer
from control import run


def run_app():
    tcp = TcpServer()

    while True:
        try:
            data = tcp.listen()
            words = data.split()
            if words and words[0] == 'POST':
                cold_mode_duration = int(words[1])
                reversed_mode_duration = int(words[2])
                cycles = int(words[3])
                run(cold_mode_duration, reversed_mode_duration, cycles)
        except Exception as ex:
            print(ex)
