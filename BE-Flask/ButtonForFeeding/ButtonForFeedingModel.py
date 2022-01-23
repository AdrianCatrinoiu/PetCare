import time
import threading
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '../ButtonForBell'))

import ButtonForBellModel

class ButtonForFeeding:
    def __init__(self, feedingPush,feedingTimer,bellTimer, feedingType):
        """
            feedingPush -> int, a value between 0 and 100 to let water or food in bowl
            feedingTimer -> set a value in seconds for feeding interval
            bellTimer -> set a value in seconds how time the bell sings
            feedingType -> Water or Food
        """
        feedingPush,feedingTimer,bellTimer = self.__validateData(feedingPush,feedingTimer,bellTimer)

        self.__bellButton = ButtonForBellModel.ButtonForBell(bellTimer, feedingType)
        self.__feedingType = feedingType
        self.__feedingLevel = 0
        self.__maxfeedingLevel = 100
        self.__feedingPush = feedingPush
        self.__feedingTimer = feedingTimer
        self.__isActive = False

    def __validateData(self,feedingPush,feedingTimer,bellTimer):
        if feedingPush <= 0:
            feedingPush = 1
        if feedingPush > 100:
            feedingPush = 100
        if feedingTimer < 0:
            feedingTimer = 1
        if feedingTimer > 100:
            feedingTimer = 100
        if bellTimer < 0:
            bellTimer = 1
        if bellTimer > 10:
            bellTimer = 10
        return (feedingPush,feedingTimer,bellTimer)
    
    def __verifyFeedingLevel(self):
        return self.__feedingLevel + self.__feedingPush <= self.__maxfeedingLevel
    
    def __addFeeding(self):
        """
            In momentul in care a ajuns la maxim, se opreste threadul ce hraneste/ ofera apa animalului
        """
        if self.__verifyFeedingLevel():
            self.__feedingLevel += self.__feedingPush
        else:
            self.__feedingLevel = self.__maxfeedingLevel
            self.__isActive = False
        
        self.__bellButton.startSinging()
    
    def getFeedingLevel(self):
        return self.__feedingLevel
    
    def startSensor(self):
        """
            La fiecare 5 secunde verificam nivelul apei din bol sa vedem daca este cazul sa mai adaugam sau nu
        """
        activeStatus = self.__isActive
        self.__isActive = True
        if not activeStatus:
            self.thread =threading.Thread(target=self.__pushIntervalFeeding, args= ())
            self.thread.start()
    
    def __pushIntervalFeeding(self):
        while(self.__isActive):
            time.sleep(self.__feedingTimer)
            self.__addFeeding()

    def stopSensor(self):
        self.__isActive = False
    
    def makeFeedingEmpty(self):
        self.__feedingLevel = 0