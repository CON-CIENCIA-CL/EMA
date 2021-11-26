from time import sleep
from serial import Serial

class SharpPM10:
    def __init__(self):
        self.serial = Serial('/dev/ttyS0', 9600, timeout=1)

    def read(self):
        with self.serial as ino:
            sleep(0.1)
            if ino.isOpen():
                if ino:
                    pckt = ino.readline().decode('utf-8').rstrip()
                    ino.flushInput()
                    if pckt:
                        return pckt
            else:
                return '--'

