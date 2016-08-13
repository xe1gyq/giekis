#!/usr/bin/python

import atexit
import ConfigParser
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from wit import Wit

from core.xwolfram import askWolfram

credentials = ConfigParser.ConfigParser()
credentialsfile = "core/configuration/credentials.config"
credentials.read(credentialsfile)

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)
relay = grove.GroveRelay(2)

def functionLight(bot, update):
    luxes = light.value()
    bot.sendMessage(update.message.chat_id, text='Light ' + str(luxes))

def functionSpeaker(bot, update):
    speaker.playSound('c', True, "med")
    bot.sendMessage(update.message.chat_id, text='Sound Reproduced!')

def functionEcho(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

    credential = credentials.get("telegram", "token")
    updater = Updater(credential)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("light", functionLight))
    dp.add_handler(CommandHandler("speaker", functionSpeaker))
    dp.add_handler(MessageHandler([Filters.text], functionEcho))

    updater.start_polling()

    while True:

        luxes = light.value()
        luxes = int(luxes)    
        display.setColor(luxes, luxes, luxes)
        display.clear()

        if button.value() is 1:
            display.setColor(255, 0, 0)
            message = "Hi! I'm GiekIe!"
            display.setCursor(0,0)
            display.write(str(message))
            relay.on()
            time.sleep(1)
            relay.off()

    updater.idle()

'''
        luxes = light.value()
        display.setColor(255, 0, 0)
        display.setCursor(0,0)
        display.write('Light ' + str(luxes))
        print 'Light ' + str(luxes)
        time.sleep(1)
'''
