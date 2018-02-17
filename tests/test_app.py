import unittest
from app.cli import URL
from app.cli import validate_count
 
class TestApp(unittest.TestCase):
    def setUp(self):
        self.url = URL()
 
    def test_1(self):
        self.assertTrue(True)
 
    def test_2(self):
        self.assertTrue(True)
 
    def test_3(self):
        self.assertEqual(self.url.name, 'url')