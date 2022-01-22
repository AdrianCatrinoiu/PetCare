from distutils.log import debug
from flask import Flask
import os
from objects import PetCareObject

petCareObject = PetCareObject()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

"""
	Rutele pentru butonul de apa
"""

@app.route('/start-water-sensor')
def startWaterSensor():
	petCareObject.startWaterSensor()
	return 'Water sensor is opened'

@app.route('/stop-water-sensor')
def stopWaterSensor():
	petCareObject.stopWaterSensor()
	return 'Water sensor is closed'

@app.route('/get-water-level')
def getWaterLevel():
	waterLevel = petCareObject.getWaterLevel()
	return f'Your water level is {waterLevel}.'

@app.route('/make-water-empty')
def makeWaterEmpty():
	petCareObject.makeWaterEmpty()
	return 'make water empty'

"""
	Buton pentru hranire
"""

@app.route('/start-food-sensor')
def startFoodSensor():
	petCareObject.startFoodSensor()
	return 'Food sensor is opened'

@app.route('/stop-food-sensor')
def stopFoodSensor():
	petCareObject.stopFoodSensor()
	return 'Food sensor is closed'

@app.route('/get-food-level')
def getFoodLevel():
	foodLevel = petCareObject.getFoodLevel()
	return f'Your food level is {foodLevel}.'

@app.route('/make-food-empty')
def makeFoodEmpty():
	petCareObject.makeFoodEmpty()
	return 'make food empty'

if __name__ == '__main__':
	os.environ['FLASK_ENV'] = 'development'
	app.run(debug=True)
