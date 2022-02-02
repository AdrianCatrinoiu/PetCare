from unittest import TestCase
import requests

class IntegrationTest(TestCase):
    
    def setUp(self):
        self.port = 'http://127.0.0.1:5000/'
    
    def test_application(self):
        # Test water ports
        waterPort = self.port + '/water'