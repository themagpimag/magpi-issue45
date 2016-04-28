#!/usr/bin/env python

import time

from gpiozero import Button

from neopixel import *

button = Button(21)

# LED strip configuration:
LED_COUNT   = 16      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin
LED_FREQ_HZ = 800000  # LED signal frequency in hertz
LED_DMA     = 5       # DMA channel to use for generating signal
#LED_BRIGHTNESS = 255  # LED brightness
LED_INVERT  = False   # True to invert the signal

# Function to control colour change

def Megalovania(strip, color):
    iterations = 0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

Megalovania(strip, Color(255,255,255))
time.sleep(2)

while True:
    Megalovania(strip, Color(0,0,0)) # Eyes off
    time.sleep(0.5)
    button.wait_for_press()
    Megalovania(strip, Color(0,0,255)) # Blue eye
    time.sleep(0.5)
    button.wait_for_press()
    time.sleep(0.5)
    while button.is_pressed == False:
        Megalovania(strip, Color(255,255,0)) # Yellow eye
        time.sleep(0.1)
        Megalovania(strip, Color(0,0,255)) # Blue eye
        time.sleep(0.1)
