import unittest as test
import ButtonForBellModel
import time

class ButtonBellTest(test.TestCase):
    """
        Clasa ce testeaza clasa ButtonBell;
        Pentru fiecare clasa vom face diferite teste in functie de ce functii are
    """

    def setUp(self):
        # Aici vom face o instanta a clasei noastre pe care vrem sa o testam
        self.bellButton = ButtonForBellModel.ButtonForBell(1)

    def test_sensor(self):
        """
            Aceasta functie ar trebui sa verifice daca clopotelul functioneaza
        """
        self.bellButton.startSinging()
        time.sleep(2)
        self.assertEqual(self.bellButton.singingStatus(), False, "The ring is not singing")

    

if __name__ == '__main__':
    test.main()
