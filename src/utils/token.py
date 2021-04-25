from .token_type import TokenType
from .position import Position


class Token:

    SPECIAL_CHARS = [';', '"', '\'', '-', '.', ',', '/', '\\', '_', '$', ' ']
    MAX_IDENTIFIER_LEN = 120
    MAX_NUMBER = 2**32

    def __init__(self, token_type: TokenType, position=None, value=None):

        self._token_type = token_type
        self._position = position
        self._value = value


    def get_token_type(self):
        return self._token_type

    def get_position(self):
        return self._position


    def get_value(self):
        return self._value
    # TODO: get string value
    # TODO: get float value


    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        else:
            return self.get_token_type() == other.get_token_type() and self.get_position() == other.get_position()

    # for testing purposes
    def __repr__(self):
        return f"TOKEN(type: {self._token_type}, position: {self._position}, value: '{self._value}')"