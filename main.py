#!/usr/bin/python

import atexit
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_i2clcd as lcd

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

light = grove.GroveLight(0)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)

def functionLight(bot, update):
    luxes = light.value()
    bot.sendMessage(update.message.chat_id, text='Light ' + str(luxes))

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

    updater = Updater("227111423:AAHgN0MRCTAAdlOPn_vQ0aVQLdxn0hYFUx0")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("light", functionLight))
    dp.add_handler(MessageHandler([Filters.text], functionEcho))

    updater.start_polling()

    while True:

        luxes = light.value()

        display.setColor(255, 0, 0)

        display.setCursor(0,0)
        display.write('Light ' + str(luxes))
        print 'Light ' + str(luxes)

        time.sleep(1)

    updater.idle()
