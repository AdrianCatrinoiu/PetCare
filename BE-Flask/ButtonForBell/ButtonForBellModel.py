import time, sys, os
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), '../TimerForSleeping'))

from TimerForSleepingModel import Timer


class ButtonForBell:
    def __init__(self, bellTimer, feedingType):
        self.__bellTimer = bellTimer
        self.__feedingType = feedingType
        self.__isActive = False
        self.timer = Timer()

    def __singing(self):
        self.__isActive = True
        time.sleep(self.__bellTimer)
        self.__isActive = False

    def startSinging(self):
        if not self.__isActive:
            threading.Thread(target=self.__singing).start()

    def singingStatus(self):
        return self.__isActive
