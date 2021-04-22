from src.data_source.file_source import FileSource
import unittest


class TestFileSource(unittest.TestCase):

    def test_file_source_greeting(self):
        self.assertEqual(FileSource().greetings(), "Hello from the FileSource")