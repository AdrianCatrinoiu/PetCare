import unittest as test
import ButtonForThermometerModel
import time

class ButtonThermometerTest(test.TestCase):
    '''
        Clasa ce testeaza clasa ButtonForThermometer
    '''
    def setUp(self):
        self.thermometerButton = ButtonForThermometerModel.ButtonForThermometer(1,23)

    def test_sensor(self):
        self.thermometerButton.startSensor()
        time.sleep(3)
        self.assertEqual(self.thermometerButton.getTemp(), 23, 'Temperature should be 23')
        self.thermometerButton.stopSensor()

    def test_temp_set(self):
        self.thermometerButton.startSensor()
        self.thermometerButton.setTempHardware(28)
        time.sleep(3)
        self.assertEqual(self.thermometerButton.getTemp(), 28, 'Temperature should be 28')
        self.thermometerButton.stopSensor()

if __name__ == "__main__":
    test.main()