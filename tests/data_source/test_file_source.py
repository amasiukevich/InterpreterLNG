from src.data_source.string_source import BaseSource
from src.data_source.string_source import StringSource
import unittest


class TestFileSource(unittest.TestCase):

    def test_file_source_getting(self):

        string = "This house is not for sale"
        ss = StringSource(string)
        symbols = []
        c = ss.get()
        while c != BaseSource.EOF:
            symbols.append(c)
            c = ss.get()

        self.assertListEqual(symbols, [c for c in string])


    def test_source_pointing_first(self):

        string = "Those houses are for sale"

        ss = StringSource(string)

        c = ss.get()
        self.assertEqual(c, "T")
