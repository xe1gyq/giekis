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

# from core.xcamera import takePhoto
# from core.xfacerecognition import recognizeFaces
from core.xspeechrecognition import recognizeSpeech
from core.xsay import isay
from core.xvoice import recordAudio
from core.xvoice import playAudio
from core.xwolfram import askWolfram

credentials = ConfigParser.ConfigParser()
credentialsfile = "core/configuration/credentials.config"
credentials.read(credentialsfile)
button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)
speaker = upmGrovespeaker.GroveSpeaker(6)

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

def say(session_id, context, msg):
    print(msg)

def merge(session_id, context, entities, msg):
    return context

def error(session_id, context, e):
    print(str(e))

def witaiLight(session_id, context):
    luxes = light.value()
    message = "Light value is " + str(luxes)
    isay("english", message)    
    context['forecast'] = 'sunny'
    return context

def witaiSpeaker(session_id, context):
    print "Play Sound"
    speaker.playSound('c', True, "med")
    context['forecast'] = 'sunny'
    return context

actions = {
    'say': say,
    'merge': merge,
    'error': error,
    'witaiLight': witaiLight,
    'witaiSpeaker': witaiSpeaker
}

if __name__ == '__main__':

    credential = credentials.get("telegram", "token")
    updater = Updater(credential)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("light", functionLight))
    dp.add_handler(CommandHandler("speaker", functionSpeaker))
    dp.add_handler(MessageHandler([Filters.text], functionEcho))

    updater.start_polling()

    credential = credentials.get("witai", "ServerAccessToken")
    client = Wit(credential, actions)

    session_id = 'my-user-id-42'

    while True:

        luxes = light.value()
        luxes = int(luxes)    
        display.setColor(luxes, luxes, luxes)

        if button.value() is 1:
            isay("english", "Hi! This is GiekIe! How can I help?")
            message = recognizeSpeech()
            display.clear()
            display.setCursor(0,0)
            display.write(str(message))
            client.run_actions(session_id, message, {})

    #updater.idle()

'''
        luxes = light.value()
        display.setColor(255, 0, 0)
        display.setCursor(0,0)
        display.write('Light ' + str(luxes))
        print 'Light ' + str(luxes)
        time.sleep(1)
'''
