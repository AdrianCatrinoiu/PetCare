import unittest as test
import ButtonWaterModel
import time

class ButtonWaterTest(test.TestCase):
    """
        Clasa ce testeaza clasa ButtonWater;
        Pentru fiecare clasa vom face diferite teste in functie de ce functii are
    """

    def setUp(self):
        # Aici vom face o instanta a clasei noastre pe care vrem sa o testam
        self.waterButton = ButtonWaterModel.ButtonWater()

    def test_sensor(self):
        """
            Aceasta functie ar trebui sa verifice daca senzorul functioneaza optim
        """
        self.waterButton.makeWaterEmpty()
        self.waterButton.startSensor()
        time.sleep(20)
        self.waterButton.stopSensor()
        self.assertEqual(self.waterButton.getWaterLevel(), 30, 'Water level should be 30.')
    

if __name__ == '__main__':
    test.main()