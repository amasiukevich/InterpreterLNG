from src.data_source.base_source import BaseSource
from src.exceptions.source_exception import SourceException
import io

class Scanner:

    def __init__(self, source: BaseSource):

        if not isinstance(source, BaseSource):
            raise SourceException("The source given is not the instance of BaseSource")
        self._source = source
        self._current_char = self._source.get()

        print("Successfully initialized source")


    def next_token(self):
        self.ignore_whitespaces()
        pass

    def ignore_whitespaces(self):
        while self._current_char.isspace():
            self._current_char = self._source.get()

    def greetings(self):
        return "Just initialized a scanner class"
