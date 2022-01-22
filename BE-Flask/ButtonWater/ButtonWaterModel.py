import time
import threading

class ButtonWater:
    def __init__(self):
        self.__waterLevel = 0
        self.__maxWaterLevel = 100
        self.__waterPush = 10
        self.__isActive = False
    
    def __verifyWaterLevel(self):
        return self.__waterLevel + self.__waterPush <= self.__maxWaterLevel
    
    def __addWater(self):
        if self.__verifyWaterLevel():
            self.__waterLevel += self.__waterPush
    
    def getWaterLevel(self):
        return self.__waterLevel
    
    def startSensor(self):
        """
            La fiecare 5 secunde verificam nivelul apei din bol sa vedem daca este cazul sa mai adaugam sau nu
        """
        activeStatus = self.__isActive
        self.__isActive = True
        if not activeStatus:
            self.thread =threading.Thread(target=self.__pushIntervalWater, args= ())
            self.thread.start()
    
    def __pushIntervalWater(self):
        while(self.__isActive):
            time.sleep(5)
            self.__addWater()

    def stopSensor(self):
        self.__isActive = False
    
    def makeWaterEmpty(self):
        self.__waterLevel = 0