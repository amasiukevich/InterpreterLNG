from src.data_source.base_source import BaseSource
from src.exceptions.source_exception import SourceException
from src.utils.token import Token
from src.utils.token_type import TokenType
import io

class Scanner:

    def __init__(self, source: BaseSource):

        if not isinstance(source, BaseSource):
            raise SourceException("The source given is not the instance of BaseSource")
        self._source = source
        self._token = Token(TokenType.UNKNOWN)
        self._current_char = self._source.get()

        self.next_token()


    def next_token(self):
        self.ignore_whitespaces()
        pass

    def ignore_whitespaces(self):
        while self._current_char.isspace():
            self._current_char = self._source.get()

    def construct_identifier(self):
        pass

    def construct_eof(self):
        pass

    def construct_string_literal(self):
        pass

    def construct_number(self):
        pass

    def construct_double_operator(self):
        pass

    def construct_integer(self):
        pass

    def construct_float(self):
        pass

    # TODO: table of keywords
    def build_keyword(self):
        pass

    def greetings(self):
        return "Just initialized a scanner class"
