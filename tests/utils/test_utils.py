from src.utils.position import Position
import unittest

class TestPosition(unittest.TestCase):

    def test_position_greetings(self):
        self.assertEqual(Position().greetings(), "Hello from the Position")