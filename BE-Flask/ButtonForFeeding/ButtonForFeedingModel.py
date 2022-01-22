import time
import threading

class ButtonForFeeding:
    def __init__(self, feedingPush,feedingTimer, feedingType):
        self.__feedingType = feedingType
        self.__feedingLevel = 0
        self.__maxfeedingLevel = 100
        self.__feedingPush = feedingPush
        self.__feedingTimer = feedingTimer
        self.__isActive = False
    
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