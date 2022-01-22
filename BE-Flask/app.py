from distutils.log import debug
from flask import Flask
import sys, os

#aici vom importa fisierele la care lucram pentru a face diferitele elemente
sys.path.insert(0,'/ButtonWater/ButtonWaterModel')

#aici vom importa fisierele
from objects import PetCareObject

#aici vom declara obiectele
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
	petCareObject.startSensor()
	return 'Water sensor is opened'

@app.route('/stop-water-sensor')
def stopWaterSensor():
	petCareObject.stopSensor()
	return 'Water sensor is closed'

@app.route('/get-water-level')
def getWaterLevel():
	waterLevel = petCareObject.getWaterLevel()
	return f'Your water level is {waterLevel}.'

@app.route('/make-water-empty')
def makeWaterEmpty():
	petCareObject.makeWaterEmpty()
	return 'make water empty'

if __name__ == '__main__':
	os.environ['FLASK_ENV'] = 'development'
	app.run(debug=True)
