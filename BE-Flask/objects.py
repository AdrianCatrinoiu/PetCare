import sys, os

#aici vom importa fisierele la care lucram pentru a face diferitele elemente
sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForThermometer'))

#aici vom importa fisierele
import ButtonForFeedingModel
import ButtonForThermometerModel

#vom crea un obiect mare ce va include toate obiectele noastre si il vom folosi in main.py
class PetCareObject:
    def __init__(self):
        self.__buttonWater = ButtonForFeedingModel.ButtonForFeeding(10,5,1,'Water')
        self.__buttonFood = ButtonForFeedingModel.ButtonForFeeding(25,20,2,'Food')
        self.__buttonThermometer = ButtonForThermometerModel.ButtonForThermometer(1)

    """
    Aici vor fi functiile pentru senzorul de apa si pentru buton
    """

    def stopWaterSensor(self):
        self.__buttonWater.stopSensor()

    def makeWaterEmpty(self):
        self.__buttonWater.makeFeedingEmpty()
    
    def getWaterLevel(self):
        return self.__buttonWater.getFeedingLevel()
    
    def startWaterSensor(self):
        self.__buttonWater.startSensor()
    
    """
        Aici voi avea functiile pentru senzorul de mancare
    """

    def stopFoodSensor(self):
        self.__buttonFood.stopSensor()

    def makeFoodEmpty(self):
        self.__buttonFood.makeFeedingEmpty()
    
    def getFoodLevel(self):
        return self.__buttonFood.getFeedingLevel()
    
    def startFoodSensor(self):
        self.__buttonFood.startSensor()

    """
        Aici sunt functiile pentru termometru
    """

    def startThermometerSensor(self):
        self.__buttonThermometer.startSensor()

    def stopThermometerSensor(self):
        self.__buttonThermometer.stopSensor()

    def getTemperature(self):
        return self.__buttonThermometer.getTemp()

    def newTempReading(self, temp):
        self.__buttonThermometer.setTempHardware(temp)