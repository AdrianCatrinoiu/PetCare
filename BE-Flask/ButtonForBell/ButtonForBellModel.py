import time, sys, os
import threading
import os
import sys
from playsound import playsound

sys.path.append(os.path.join(os.path.dirname(__file__), '../TimerForSleeping'))

from TimerForSleepingModel import Timer


class ButtonForBell:
    def __init__(self ,bellTimer,bellType):
        self.__bellTimer = bellTimer
        self.__isActive = False
        self.timer = Timer()
        self.__bellType = bellType
        self.__location__ =os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __singing(self):
        self.__isActive = True
        if self.__bellType == 'Food' or self.__bellType == 'Water' and not self.timer.getSoundStatus():
            try:
                playsound(os.path.join(self.__location__ , 'sound.wav'))
            except:
                pass
        time.sleep(self.__bellTimer)
        self.__isActive = False

    def startSinging(self):
        if not self.__isActive:
            threading.Thread(target=self.__singing).start()

    def singingStatus(self):
        return self.__isActive
