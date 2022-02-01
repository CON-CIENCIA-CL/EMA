import serial
from sys import path
from time import sleep
##
from components.setups import SDL_Pi_HDC1080
from components.LCD_1602 import LCD
from components.RGB_LED import RGB

path.append('./SDL_Pi_HDC1080_Python3')

class Test:
  def __init__(self):
    self.aux = ''
    try:
      self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()
      self.aux = '[ - ] HDC importado'
      self.lcd = LCD()
      self.aux = '[ - ] LCD importado'
      self.rgb = RGB()
      self.aux = '[ - ] RGB importado'

    except Exception as e:
      print(f"\n[ ! ] Fallo en {self.aux}: {e}\n")


  def _SHARP(self):
    print("\n[ ! ] Inicializando conexion serial ...")
    with serial.Serial('/dev/ttyS0', 9600, timeout=1) as arduino:
      print("[ ! ] Revisando conexion serial")

      if arduino.isOpen():
        print(f"[ ok ] Sensor {arduino} conectado")

        for i in range(3):
          if arduino:
            print("[ - ] Esperando datos del sensor")
            line = arduino.readline().decode('utf-8').rstrip()
            print(f"[ ! ] Lectura de prueba {i/3}: {line}")
            sleep(1)
            arduino.flushInput()
          else:
            print("[ ! ] Sensor en stand-by")
      else:
        print("[ ! ] Fuera de flujo al revisar conexion serial")
      
      print("[ ok ] Test de modulo SHARP completado.\n")


  def _LED(self, delay=1):
    for i in range(3):
      try:
        print(f"\n[ ! ] Inicializando testeo {i/3} para RGB Led")
        print("[ - ] Probando verde ON")
        self.rgb.greenOn()
        sleep(delay)
        print("[ - ] Probando verde OFF")
        self.rgb.greenOff()

        print("[ - ] Probando amarillo ON")
        self.rgb.yellowOn()
        sleep(delay)
        print("[ - ] Probando amarillo OFF")
        self.rgb.yellowOff()

        print("[ - ] Probando rojo ON")
        self.rgb.redOn()
        sleep(delay)
        print("[ - ] Probando rojo OFF")
        self.rgb.redOff()
      
      except Exception as e:
        print(f"[ ! ] {e}")

    print("[ ok ] Test de modulo SHARP completado.\n")

  def _LCD(self):
    for i in range(3):
      try:
        self.lcd.clear()
        print(f"\n[ ! ] Inicializando testeo {i/3} para modulo LCD")
        print("[ - ] Apagando Blacklight ...")
        self.lcd.BlacklightOff()
        sleep(2)
        print("[ - ] Encendiendo Blacklight ...")
        self.lcd.BlacklightOn()
        sleep(2)
        print("[ - ] Imprimiendo en display ...")
        self.lcd.Base('[ ok ] Hello world!', 1)
        sleep(2)
      except Exception as e:
        print(f"\n[ ! ] {e}")

    print("[ ok ] Test de modulo display LCD completado.\n")


  def _HDC(self):
    for i in range(3):
      try:
        print(f"[ - ] Obteniendo lectura para Temperatura {i/3}: {self.hdc1080.readTemperature()}")
        sleep(2)
        print(f"[ - ] Obteniendo lectura para Humedad {i/3}: {self.hdc1080.readHumidity()}")
        sleep(2)
      except Exception as e:
        print(f"\n[ ! ] {e}")


if __name__ == '__main__':
  testing = Test()
  testing._SHARP()
  testing._LED()
  testing._LCD()
  testing._HDC()
