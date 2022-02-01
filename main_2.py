from components.HDC_1080 import HDC
from componetns.RGB_LED import RGB
from components.SHARP_PM10 import SharpPM10

class EMA:
    def __init__(self):
        self.hdc = HDC()
        self.rgb = RGB()
        self.pm10 = SharpPM10()

    def get_hdc_data(self):
        temperature = self.hdc.get_temperature()
        humidity = self.hdc.get_humidity()
        data = {
            'temperature': temperature,
            'humidity': humidity,
        }
        return data

    def get_sharp_pm10_data(self):
        pm10 = self.pm10.read()
        data = {
            'pm10': pm10,
        }
        return data

    def read_dust(self):
        dust = self.get_sharp_pm10_data()
        # 0 - 54 -> 
        if 0 <= dust['pm10'] <= 54:
            self.rgb.set_color(0, 255, 0)
            
            self.rgb.redOff()
            self.rgb.greenOff()
            self.rgb.yellow()
            self.rgb.greenOn()

        # 50 - 100 ->
        elif 54 < dust['pm10'] <= 154:
            self.rgb.set_color(255, 255, 0)

            self.rgb.redOff()
            self.rgb.greenOff()
            self.rgb.yellowOff()
            self.rgb.yellowOn()

        # 100 - 150 ->
        elif 154 < dust['pm10']:
            self.rgb.set_color(255, 165, 0)
            
            self.rgb.redOff()
            self.rgb.greenOff()
            self.rgb.yellowOff()
            self.rgb.redOn()

        return dust.pm10

if __name__ == '__main__':
    ema = EMA()
    ema.read_dust()

    print("Temperatura: {}".format(ema.get_hdc_data()['temperature']))
    print("Humidad: {}".format(ema.get_hdc_data()['humidity']))
    print("PM10: {}".format(ema.get_sharp_pm10_data()['pm10']))
