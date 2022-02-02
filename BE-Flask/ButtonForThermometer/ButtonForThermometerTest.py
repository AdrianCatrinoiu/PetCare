import unittest as test
import ButtonForThermometerModel
import time

class ButtonThermometerTest(test.TestCase):
    '''
        Clasa ce testeaza clasa ButtonForThermometer
    '''
    def setUp(self):
        self.thermometerButton = ButtonForThermometerModel.ButtonForThermometer(4,23)

    def test_sensor(self):
        self.thermometerButton.startSensor()
        time.sleep(5)
        self.thermometerButton.stopSensor()
        self.assertEqual(self.thermometerButton.getTemp(), 23, 'Temperature should be 23')

    def test_temp_set(self):
        self.thermometerButton.startSensor()
        self.thermometerButton.setTempHardware(28)
        time.sleep(5)
        self.thermometerButton.stopSensor()
        self.assertEqual(self.thermometerButton.getTemp(), 28, 'Temperature should be 28')

if __name__ == "__main__":
    test.main()