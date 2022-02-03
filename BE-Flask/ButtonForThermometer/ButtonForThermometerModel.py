import time
import threading, sys, os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db_v2 import DB

def addInDb(level,DB):
    DB.addInTable('Temperature',level)

f = open('paramConfig.json')
parameterConfig = json.load(f)
parameterConfig = parameterConfig['thermometer']


class ButtonForThermometer:
    def __init__(self, updateRate=parameterConfig['updateRate'], tempInit=parameterConfig['tempInit']):
        self.DB = DB()
        self.DB.createTables()
        self.__temperature = None
        self.__isActive = False
        self.__updateRate = updateRate
        self.__tempHardware = tempInit

    def startSensor(self):
        self.__isActive = True

        if self.__isActive:
            self.thread = threading.Thread(target=self.__setTemp, args=())
            self.thread.start()

    def stopSensor(self):
        self.__isActive = False
    
    def __setTemp(self):
        while self.__isActive:
            time.sleep(self.__updateRate)
            self.__temperature = self.__tempHardware
            addInDb(self.__temperature,self.DB)

    def getTemp(self):
        if self.__isActive:
            return self.__temperature

    def setTempHardware(self, temp):
        if self.__isActive:
            self.__tempHardware = temp
            return temp
            
    def getStatus(self):
        return self.__isActive