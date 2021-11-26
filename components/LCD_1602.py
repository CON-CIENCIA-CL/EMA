#! /usr/bin/env python

# Simple string program. Writes and updates strings.


# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel
# Backlight: Enhanced by TOMDENKT - backlight control (on/off)
# Backlight: lcd_backlight(1) = ON, lcd_backlight(0) = OFF
# Backlight: Usage, if lcddriver is set to "display" (like example below)
# Backlight: display.lcd_backlight(0) # Turn backlight off
# Backlight: display.lcd_backlight(1) # Turn backlight on

import modules.setups.lcd.settings as drivers
from time import sleep

display = drivers.Lcd()

def clear():
    display.lcd_clear()

def BacklightOn():
    display.lcd_backlight(1) # Make sure backlight is on / turn on

def BacklightOff():
    display.lcd_backlight(0) # Turn backlight off

def Base(text, line):
    # Remember that your sentences can only be 16 characters long!
    print("Enviando a pantalla ...")
    display.lcd_display_string(text, line)  # Write line of text to first line of display

def Scroll(text, line):
    print("Press CTRL + C to stop this script!")

    def long_string(display, string='', num_line=1, num_cols=20):
        """ 
        Parameters: (driver, string to print, number of line to print, number of columns of your display)
        Return: This function send to display your scrolling string.
        """
        
        if len(string) > num_cols:
            display.lcd_display_string(string[:num_cols], num_line)
            sleep(1)
            for i in range(len(string) - num_cols + 1):
                text_to_print = string[i:i+num_cols]
                display.lcd_display_string(text_to_print, num_line)
                sleep(0.2)
            sleep(1)

        else:
            display.lcd_display_string(string, num_line)

    long_string(display, text, line)
