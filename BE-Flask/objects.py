import sys, os

#aici vom importa fisierele la care lucram pentru a face diferitele elemente
sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonWater'))

#aici vom importa fisierele
import ButtonWaterModel

#vom crea un obiect mare ce va include toate obiectele noastre si il vom folosi in main.py
class PetCareObject:
    def __init__(self):
        self.__buttonWater = ButtonWaterModel.ButtonWater()

    """
    Aici vor fi functiile pentru senzorul de apa si pentru buton
    """

    def stopSensor(self):
        self.__buttonWater.stopSensor()

    def makeWaterEmpty(self):
        self.__buttonWater.makeWaterEmpty()
    
    def getWaterLevel(self):
        return self.__buttonWater.getWaterLevel()
    
    def startSensor(self):
        self.__buttonWater.startSensor()