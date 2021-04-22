from src.scanner.scanner import Scanner
import unittest

class TestScanner(unittest.TestCase):

    def test_scanner_greetings(self):
        self.assertEqual(Scanner().greetings(), "Just initialized a scanner class")

    def test_scanner_skip_whitespaces(self):
        self.assertEqual(Scanner().skip_whitespaces("Skipping whitespaces"), "Skippingwhitespaces")