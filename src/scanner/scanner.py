from src.data_source.base_source import BaseSource
import io

class Scanner:

    def __init__(self, source: BaseSource):
        self.source = source

    def skip_whitespaces(self):
        return NotImplemented()

    def greetings(self):
        return "Just initialized a scanner class"
