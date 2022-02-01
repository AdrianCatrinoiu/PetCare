import time
import threading
import os
import sys
from playsound import playsound

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class ButtonForBell:
    def __init__(self ,bellTimer,bellType):
        self.__bellTimer = bellTimer
        self.__isActive = False
        self.__bellType = bellType

     
     
    def __singing(self):
       self.__isActive = True
       if self.__bellType == 'Food' or self.__bellType == 'Water':
           playsound(os.path.join(__location__, 'sound.wav'))
       time.sleep(self.__bellTimer)
       self.__isActive = False

    
    def startSinging(self):
        if not self.__isActive:
            threading.Thread(target = self.__singing).start()

    
    def singingStatus(self):
        return self.__isActive
