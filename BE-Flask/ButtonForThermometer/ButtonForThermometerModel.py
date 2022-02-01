import time
import threading
from flask import jsonify

from db import get_db

def addInDb(temp):
    if not temp:
        return jsonify({

                "status": "Temperature level is required."
            }), 403

    try:
        db = get_db()
        db.execute(
            'INSERT INTO temperature (level)'
            ' VALUES (?)',
            (temp,)
        )
        db.commit()
    except:
        print("database doesn't exist")


class ButtonForThermometer:
    def __init__(self, updateRate):
        self.__temperature = None
        self.__isActive = False
        self.__updateRate = updateRate
        self.__tempHardware = 23

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
            addInDb(self.__temperature)

    def getTemp(self):
        if self.__isActive:
            return self.__temperature

    def setTempHardware(self, temp):
        if self.__isActive:
            self.__tempHardware = temp