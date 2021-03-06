import sys, os, unittest as test

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForBell'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'TimerForSleeping'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForThermometer'))

import ButtonForFeedingTest
import ButtonForBellTest
import TimerForSleepingTest
import ButtonForThermometerTest


class UnitTests(test.TestCase):

    def setUp(self):
        self.buttonBellTest = ButtonForBellTest.ButtonBellTest()
        self.buttonFeedingTest = ButtonForFeedingTest.ButtonFeedingTest()
        self.timerTest = TimerForSleepingTest.TimerTest()
        self.buttonThermometerTest = ButtonForThermometerTest.ButtonThermometerTest()

        self.buttonBellTest.setUp()
        self.buttonFeedingTest.setUp()
        self.timerTest.setUp()
        self.buttonThermometerTest.setUp()
    
    def test_ButtonBellTests(self):
        self.buttonBellTest.test_sensor()
    
    def test_ButtonFeedingTests(self):
        self.buttonFeedingTest.test_sensor()
        self.buttonFeedingTest.test_manual_push()

    def test_TimerTests(self):
        self.timerTest.test_timer_stop_noise()
        self.timerTest.test_timer_start_noise()

    def test_ButtonThermometerTests(self):
        self.buttonThermometerTest.test_sensor()
        self.buttonThermometerTest.test_temp_set()

if __name__ == '__main__':
    test.main()