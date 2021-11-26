from numpy import median
from serial import Serial

class SharpPM10:
    def __init__(self):
        self.serial = Serial('/dev/ttyAMA0', 9600, timeout=1)

    def read(self):
        with self.serial as ino:
            if ino.isOpen():
                if ino:
                    pckt = ino.readline().decode('utf-8').rstrip()
                    if pckt:
                        return pckt
            ino.flushInput()

