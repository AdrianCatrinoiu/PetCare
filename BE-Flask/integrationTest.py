import os, sys
from unittest import TestCase, main
import requests

class IntegrationTest(TestCase):
    
    def setUp(self):
        self.port = 'http://127.0.0.1:5000/'
    
    def test_water_endpoints(self):
        '''Test water ports'''
        waterPort = self.port + '/water'
        
        #Get all water entries
        response = requests.get(waterPort)
        self.assertEqual(response.status_code, 200)

        #Start water sensor
        response = requests.post(waterPort + '/start-water-sensor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'Water sensor is opened')

        #Stop water sensor
        response = requests.get(waterPort + '/stop-water-sensor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'Water sensor is closed')
        response = requests.post(waterPort + '/stop-water-sensor')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text,'Wrong request')

        #Make water level empty
        response = requests.post(waterPort + '/make-water-empty')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'make water empty')

        #Get water level
        response = requests.post(waterPort + '/get-water-level')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text,'Wrong request')
        response = requests.get(waterPort + '/get-water-level')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'Your water level is 0.')

        #Push water
        requests.post(waterPort + '/push-water-manual')
        response = requests.get(waterPort + '/get-water-level')
        self.assertEqual(response.text, 'Your water level is 10.')


    def test_food_endpoints(self):
        '''Test food ports'''
        foodPort = self.port + '/food'
        
        #Get all food entries
        response = requests.get(foodPort)
        self.assertEqual(response.status_code, 200)

        #Start food sensor
        response = requests.post(foodPort + '/start-food-sensor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'Food sensor is opened')

        #Stop food sensor
        response = requests.get(foodPort + '/stop-food-sensor')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'Food sensor is closed')
        response = requests.post(foodPort + '/stop-food-sensor')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text,'Wrong request')

        #Make food level empty
        response = requests.post(foodPort + '/make-food-empty')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'make food empty')

        #Get food level
        response = requests.post(foodPort + '/get-food-level')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text,'Wrong request')
        response = requests.get(foodPort + '/get-food-level')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text,'Your food level is 0.')

        #Push food
        requests.post(foodPort + '/push-food-manual')
        response = requests.get(foodPort + '/get-food-level')
        self.assertEqual(response.text, 'Your food level is 25.')

    def test_sound_endpoints(self):
        #test make silence
        response = requests.post(self.port + '/make-silence')
        self.assertEqual(response.status_code,200)

        #test make noise
        response = requests.post(self.port + '/make-noise')
        self.assertEqual(response.status_code,200)
    
    def test_environment_endpoints(self):
        '''
            I will make the next flow, 
            I will start the temp sensor, In will set temp at 28C
            and I will stop sensor, after I will take current value
            of temp.
        '''
        requests.post(self.port + '/start-thermometer')
        body = {'temp': 28}
        response = requests.post(self.port + '/set-current-temperature',body)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.text,'Current temperature is: 28C')

    def test_all_untested_endpoints(self):
        # button water stauts
        response = requests.get(self.port + '/water/get-sensor-status')
        self.assertEqual(response.status_code,200)
        # button food stauts
        response = requests.get(self.port + '/food/get-sensor-status')
        self.assertEqual(response.status_code,200)
        # test sound 
        response = requests.get(self.port + '/start-timer-for-silence')
        self.assertEqual(response.text, 'Start timer to making silence')
        # get all temperatures
        response = requests.get(self.port + '/get-temperature')
        self.assertEqual(response.status_code,200) 
        # start thermometer
        response = requests.get(self.port + '/start-thermometer')
        self.assertEqual(response.status_code,200) 
        # stop thermometer
        response = requests.get(self.port + '/stop-thermometer')
        self.assertEqual(response.status_code,200)
        # start thermometer
        response = requests.get(self.port + '/get-current-temperature')
        self.assertEqual(response.status_code,200)  
        # get sensor status
        response = requests.get(self.port + '/get-sensor-status')
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    main()