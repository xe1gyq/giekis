#!/usr/bin/python

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd

from core.xspeechrecognition import recognizeSpeech
from core.xsay import isay
from core.xvoice import recordAudio
from core.xvoice import playAudio
from core.xwolfram import askWolfram

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)
speaker = upmGrovespeaker.GroveSpeaker(6)

if __name__ == '__main__':

    while True:

        luxes = light.value()
        luxes = int(luxes) 
        display.setColor(luxes, luxes, luxes)

        if button.value() is 1:
            isay("espanol", "Hola! Gracias por tirar tu basura!")
            display.clear()
            display.setCursor(0,0)
            display.write("Basura Depositada!")
