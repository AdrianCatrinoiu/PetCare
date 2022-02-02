from time import sleep
import unittest as test
from TimerForSleepingModel import Timer

class TimerTest(test.TestCase):

    def setUp(self):
        self.__timer = Timer(1)
    
    def test_timer_stop_noise(self):
        self.__timer.startTimer()
        sleep(2)
        self.assertEqual(self.__timer.getSoundStatus(), True, ' Sound status should be silence.')

    def test_timer_start_noise(self):
        self.__timer.makeNoise()
        self.assertEqual(self.__timer.getSoundStatus(), False, ' Sound status should be noise.')
    
if __name__ == '__main__':
    test.main()