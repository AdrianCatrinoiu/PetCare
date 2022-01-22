from flask import Flask
import sys

#aici vom importa fisierele la care lucram pentru a face diferitele elemente
sys.path.insert(0,'/ButtonWater/ButtonWaterModel')

#aici vom importa fisierele
import ButtonWaterModel

#aici vom declara obiectele
buttonWater = ButtonWaterModel.ButtonWater()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/start-water-sensor')
def startWaterSensor():
	buttonWater.startSensor()
	return 'Water sensor is opened'

@app.route('/stop-water-sensor')
def stopWaterSensor():
	buttonWater.stopSensor()
	return 'Water sensor is closed'

if __name__ == '__main__':
	app.run()
