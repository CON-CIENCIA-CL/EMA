import wiringpi
from numpy import median
from spidev import SpiDev


class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()

    def open(self):
        self.spi.open(self.bus, self.device)
        if not self.spi.is_open:
            raise ValueError('[!] Could not open SPI bus')

    def read(self, adc_channel = 0):
        # 0-7 channels available only
        if ((adc_channel > 7) or (adc_channel < 0)):
            return -1
        r = self.spi.xfer2([1, (8 + adc_channel) << 4, 0])
        adc_output = ((r[1] & 3) << 8) + r[2]
        
        return adc_output

    def close(self):
        self.spi.close()


class SharpPM10:
    def __init__(
        self, 
        led_pin, 
        pm10_pin, 
        adc,
        sampling_time=280, 
        delta_time=40, 
        sleep_time=9680
    ):

        if led_pin is None:
            raise ValueError('Led pin number is missing!')
        if pm10_pin is None:
            raise ValueError('PM10 pin number is missing!')

        if not adc:
            self.adc = MCP3008()
        else:
            self.adc = adc

        self.led_pin = led_pin
        self.pm10_pin = pm10_pin

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(led_pin, 1)
        wiringpi.digitalWrite(led_pin, 0)

        self.sampling_time = sampling_time
        self.delta_time = delta_time
        self.sleep_time = sleep_time

    
    def read(self):
        wiringpi.digitalWrite(self.led_pin, 1) # power on the LED
        wiringpi.delayMicroseconds(self.sampling_time)
        wiringpi.delayMicroseconds(self.delta_time)
        vo_measured = self.adc.read(self.pm10_pin) # read the dust value
        wiringpi.digitalWrite(self.led_pin, 0) # turn the LED off

        # Voltage 0 - 5V mapped to 0 - 1023 integer values
        calc_voltage = vo_measured * (5.0 / 1024)

        # linear eqaution taken from http://www.howmuchsnow.com/arduino/airquality/ (Chris Nafis (c) 2012)
        dust_density = 0.17 * calc_voltage - 0.1

        return dust_density


    def readSequence(self):
        vo_measured = 0
        readings = []

        for i in range(10):
            wiringpi.digitalWrite(self.led_pin, 1) # power on the LED
            wiringpi.delayMicroseconds(self.sampling_time)
            wiringpi.delayMicroseconds(self.delta_time)
            vo_measured = self.adc.read(self.pm10_pin) # read the dust value
            wiringpi.digitalWrite(self.led_pin, 0) # turn the LED off

            wiringpi.delayMicroseconds(self.sleep_time) # wait 9.68ms before the next sequence is repeated

            # Voltage 0 - 5V mapped to 0 - 1023 integer values
            calc_voltage = vo_measured * (5.0 / 1024)

            # linear eqaution taken from http://www.howmuchsnow.com/arduino/airquality/ (Chris Nafis (c) 2012)
            dust_density = 0.17 * calc_voltage - 0.1
            readings.append(dust_density)

        return median(readings)

def test():
    try:
        ADC = MCP3008() # CE0
    except TypeError:
        raise TypeError('[!] Could not open SPI bus; Error setting up MCP3008 class')
    
    pm10 = SharpPM10(led_pin=21, pm10_pin=1, adc=ADC)
    if not pm10:
        raise ValueError('[!] Could not initialize SharpPM10 class')

    print('[+] Testing the SharpPM10 class')
    print('[+] Reading the dust value')
    print('[*] Value:', pm10.read())
    print('[+] Reading the dust value')
    print('[*] Value:', pm10.readSequence())
    print('[+] Testing the SharpPM10 class')

    ADC.close()

test()

#! MANU'S SCRIPT
import serial
import time

if __name__ == '__main__':
    print("abriendo conexion serial")
    with serial.Serial('/dev/ttyS0', 9600, timeout=1) as arduino:
        time.sleep(0.1)
        
        if arduino.isOpen():
            print("sensor {} conectado".format(arduino))
            while True:
                if arduino:
                    print("esperando datos del arduino")
                    line = arduino.readline().decode('utf-8').rstrip()
                    print("lectura: {}".format(line))
                    time.sleep(1)
                    arduino.flushInput()
                else:
                    print("arduino no en espera")


