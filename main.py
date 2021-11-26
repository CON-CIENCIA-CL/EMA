# Importando librerias de modulos y sensores
from components.RGB_LED import *
from components.MCP_3008 import Mcp3008
from components.SHARP_PM10 import SharpPM10
from components.HDC_1080 import HDCtemp, HDChum
from components.LCD_1602 import Base, Scroll, BacklightOn, BacklightOff, clear

# Importando librerias de Python 3
from time import *
import sys

try:
    ADC = Mcp3008() # CE0
except TypeError:
    raise TypeError('[!] Could not open SPI bus; Error setting up MCP3008 class')

pm10 = SharpPM10(led_pin=21, pm10_pin=1, adc=ADC) # Obteniendo lectura de voltaje

def testSharpPM10():
    if not pm10:
        raise ValueError('[!] Could not initialize SharpPM10 class')
    
    print('[+] Testing the SharpPM10 class')
    print('[+] Reading the dust value')
    print('[*] Value :', pm10.read())
    print('[+] Reading the dust value')
    print('[*] Value :', pm10.readSequence())
    print('[+] Reading the dust value')
    print('[*] Value :', pm10.read())
    print('[+] Reading the dust value')
    print('[*] Value :', pm10.readSequence())

    ADC.close()

def test():
    testSharpPM10()

def data(): # Funcion de recoleccion de datos
    BacklightOn() # Encendiendo luces del Display

    clear()
    Base(f'PM2.5: {pm10.read()}', 1) # Imprimiendo densidad de polvo en el Display (1era linea)
    Base(f'PM10: {pm10.read()}', 2) # Imprimiendo densidad de polvo en el Display (2da linea)

    # Cambiando de textos, apagando, limpiando y encendiendo el Display
    sleep(2)
    BacklightOff() # Apagado
    clear() # Limpiar
    BacklightOn() # Encendido

    Base(f'Temp: {HDCtemp(3)} {chr(223)}C', 1) # Impripiendo en Display la temeratura actual
    Base(f'Hume: {HDChum(3)} %', 2) # Imprimiendo en el Display la humedad actual
    sleep(2) # Se esperan 2 segundos antes de continuar

def init(): # Funcion que inicia a EMA
    clear() # Limpia el Display por si hay algo previo
    BacklightOn() # Enciende la pantalla del Display
    for i in range(4): # Enciende y apaga el Display 4 veces en medio segundo cada una
        BacklightOff()
        sleep(.05)
        BacklightOn()
        sleep(.05)
    
    Scroll('Estacion de Monitoreo', 1) # Imprimiendo scroll en la 1era linea del Display
    Scroll("            Ambiental", 2) # Imprimiendo scroll en la 2da linea del Display
    clear() # Limpiando Display
    sleep(2) # Esperando 2 segundos antes de seguir
    Base('      EMA       ', 1) # Imprimiendo en Display
    sleep(2) # Esperarndo 2 segundos antes de seguir
    clear() # Limpiando Display

    for i in range(4): # Enciende y apaga el Display 4 veces en medio segundo cada una
        BacklightOff()
        sleep(.05)
        BacklightOn()
        sleep(.05)

    Scroll('Leyendo datos de sensores ...', 1) # Imprimiendo scroll en la 1era linea

def main(args = sys.argv[1:]):
    test()
    print('[+] Initializing the EMA')

    init() # Se inicia del Display
    clear() # Se limpia el Display por si hay algo previo
    try:
        while True: # Mostraremos datos hastas que se presiones Crtl + C
            data() # Datos de sensores
    except KeyboardInterrupt: # Si se presiona Crtl + C
        clear() # Se limpia el Display
        print('\n') # Salto de linea
        exit() # El programa finaliza

if __name__ == '__main__':
    main()
