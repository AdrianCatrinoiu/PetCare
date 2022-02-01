from threading import Thread
from time import sleep

class SoundControl:
    __isSilence = False

    @classmethod
    def makeNoise(cls):
        cls.__isSilence = True
    
    @classmethod
    def makeSilence(cls):
        cls.__isSilence = False
    
    @classmethod
    def getSoundStatus(cls):
        return cls.__isSilence

class Timer:
    def __init__(self):
        self.__isActivated = False
    
    def startTimer(self):
        SoundControl.makeSilence()
        if self.__isActivated:
            return 
        self.__isActivated = True
        Thread(self.__startTimer).start()

    def __startTimer(self):
        sleep(60*self.__timer)
        self.__isActivated = False
    
    def makeNoise(self):
        self.__isActivated = False
        SoundControl.makeNoise()
        
