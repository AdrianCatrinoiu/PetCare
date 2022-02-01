from threading import Thread
from time import sleep

class SoundControl:
    __isSilence = False

    @classmethod
    def makeNoise(cls):
        cls.__isSilence = False
    
    @classmethod
    def makeSilence(cls):
        cls.__isSilence = True
    
    @classmethod
    def getSoundStatus(cls):
        print(cls.__isSilence)
        return cls.__isSilence

class Timer:
    def __init__(self, timer=60):
        self.__timer = timer
        self.soundControl = SoundControl()
        self.__isActivated = False
    
    def startTimer(self):
        self.soundControl.makeSilence()
        if self.__isActivated:
            return 
        self.__isActivated = True
        Thread(target = self.__startTimer,args= ()).start()

    def __startTimer(self):
        sleep(self.__timer)
        self.__isActivated = False
    
    def makeNoise(self):
        self.__isActivated = False
        self.soundControl.makeNoise()
    
    def makeSilence(self):
        self.__isActivated = True
        self.soundControl.makeSilence()

    def getSoundStatus(self):
        return self.soundControl.getSoundStatus()
        
