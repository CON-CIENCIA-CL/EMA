from os import system as install
from time import *

def installer():
    packages = ['sudo apt install software-properties-common -y',
    'sudo apt-get install libatlas-base-dev -y',
    'pip3 install -r EMA/components/setups/requirements.txt --force',
    'sudo apt-get update',
    'sudo sh EMA/components/setups/lcd/install.sh'
    ]


    for package in packages:
        install(package)

def main():
    confirm = input('''
    Los siguientes packetes serán instalados:\n
        update and upgrade system, EMA Official repository,
        requirement.txt (wiringpi==2.60.1-numpy-config==0.5.0.post0-spidev==3.5
        RPi.GPIO==0.7.0-smbus==1.1.post2-Adafruit_GPIO==1.0.3), lcd-calibration
    ¿Deseas continuar? [S/n] ''')
    if confirm == 'S':
        installer()
    else:
        exit()    

# sudo -s
# echo "nameserver 8.8.8.8" >> /etc/resolv.conf
# chmod 644 /etc/resolv.conf
# exit
# ping google.com
