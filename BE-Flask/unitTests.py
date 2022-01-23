import sys, os, unittest as test

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForBell'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))

import ButtonForFeedingTest
import ButtonForBellTest


class UnitTests(test.TestCase):

    def setUp(self):
        self.buttonBellTest = ButtonForBellTest.ButtonBellTest()
        self.buttonFeedingTest = ButtonForFeedingTest.ButtonFeedingTest()
    
    def test_ButtonBellTests(self):
        self.buttonBellTest.setUp()
        self.buttonBellTest.test_sensor()
    
    def test_ButtonFeedingTests(self):
        self.buttonFeedingTest.setUp()
        self.buttonFeedingTest.test_sensor()


if __name__ == '__main__':
    test.main()