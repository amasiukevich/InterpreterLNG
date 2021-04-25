from src.data_source.base_source import BaseSource
from src.utils.position_source import PositionSource
from src.exceptions.source_exception import SourceException
from src.exceptions.scanner_exception import ScannerException
from src.utils.token import Token
from src.utils.token_type import TokenType

from .keyword_mapper import KeywordMapper
import io

class Scanner:

    def __init__(self, source: BaseSource):

        if not isinstance(source, BaseSource):
            raise SourceException("The source given is not the instance of BaseSource")
        self._source = source
        self.kw_mapper = KeywordMapper()

        self._token = Token(TokenType.UNKNOWN)
        self._current_char = self._source.get()
        self._tmp_kw_id = ""
        self._tmp_len = 0

        self.next_token()


    def peek_token(self):
        return self._token

    def get_token(self):

        temp_token = self._token
        self.next_token()
        print(self._token_position)
        return temp_token



    def next_token(self):

        self.ignore_whitespaces()
        self._token_position = self._source.get_position()

        if self.construct_eof():
            return
        elif self.construct_single_char_oper():
            return
        elif self.construct_double_char_oper():
            return
        elif self.construct_number():
            return
        elif self.construct_string_literal():
            return
        elif self.construct_identifier():
            return
        else:
            self._token = Token(TokenType.UNKNOWN, position=self._token_position)
            raise ScannerException(self._token_position, "Unknown symbol")


    def ignore_whitespaces(self):
        if self._current_char != BaseSource.EOF:
            while self._current_char.isspace():
                self._current_char = self._source.get()
        else:
            return


    def construct_eof(self):

        if self._current_char == BaseSource.EOF:
            self._token = Token(TokenType.EOF, position=self._token_position)
            self._current_char = self._source.get()
            return True
        else:
            return False

        # TODO: maybe return self._current_char???

    def construct_single_char_oper(self):

        try:
            tmp_token_type = self.kw_mapper.SINGLE_CHAR_MAP[self._current_char]
            self._token = Token(tmp_token_type, value=self._current_char, position=self._token_position)
            self._current_char = self._source.get()
            return True
        except Exception as e:
            # print("Exception here ", e)
            return False


    def construct_double_char_oper(self):

        first_char = self._current_char
        recognized = True
        if first_char == "!":
            self._current_char = self._source.get()
            if self._current_char == "=":
                self._token = Token(TokenType.NOT_EQUAL, value="!=", position=self._token_position)
                self._current_char = self._source.get()
            else:
                self._token = Token(TokenType.NOT, value="!", position=self._token_position)

        elif first_char == "=":
            self._current_char = self._source.get()
            if self._current_char == "=":
                self._token = Token(TokenType.EQUAL, value="==", position=self._token_position)
                self._current_char = self._source.get()
            else:
                self._token = Token(TokenType.ASSIGN, value="=", position=self._token_position)

        elif first_char == "<":
            self._current_char = self._source.get()
            if self._current_char == "=":
                self._token = Token(TokenType.LESS_EQUAL, value="<=", position=self._token_position)
                self._current_char = self._source.get()
            else:
                self._token = Token(TokenType.LESS, value="<", position=self._token_position)

        elif first_char == ">":
            self._current_char = self._source.get()
            if self._current_char == "=":
                self._token = Token(TokenType.GREATER_EQUAL, value=">=", position=self._token_position)
                self._current_char = self._source.get()
            else:
                self._token = Token(TokenType.GREATER, value=">", position=self._token_position)

        elif first_char == "&":
            self._current_char = self._source.get()
            if self._current_char == "&":
                self._token = Token(TokenType.AND, value="&&", position=self._token_position)
                self._current_char = self._source.get()
            else:
                recognized = False

        elif first_char == "|":
            self._current_char = self._source.get()
            if self._current_char == "|":
                self._token = Token(TokenType.OR, value="|", position=self._token_position)
                self._current_char = self._source.get()
            else:
                recognized = False
        else:
            recognized = False

        return recognized

    def construct_number(self):

        if not self._current_char.isdigit():
            return False

        value = self.construct_integer()

        # constructing fraction
        frac = 0
        if self._current_char == ".":
            self._current_char = self._source.get()
            frac = self.build_fraction()

        # making token
        self._token = Token(TokenType.NUMERIC_LITERAL, value=(value + frac), position=self._token_position)
        return True


    def construct_integer(self):

        if self.is_zero_integer():
            return 0

        return self.construct_non_zero_num()

    def is_zero_integer(self):

        is_zero = False
        if self._current_char == '0':
            self._current_char = self._source.get()
            if self._current_char.isdigit():
                raise ScannerException(self._source.get_position(), "Non-zero number can't start with zero")
        return is_zero

    def construct_non_zero_num(self):

        value = 0
        while self._current_char.isdigit() and value < Token.MAX_NUMBER:
            value += 10 * value + (ord(self._current_char) - ord('0'))
            self._current_char = self._source.get()

        if self._current_char.isdigit():
            raise ScannerException(self._token_position, "Max allowed number value is 2^32")

        return value

    def build_fraction(self):

        value = 0
        exponent = self.ignore_zeros() + 1
        while self._current_char.isdigit():
            value += (ord(self._current_char) - ord('0')) / pow(10, exponent)
            exponent += 1
            self._current_char = self._source.get()

        return value



    def ignore_zeros(self):
        num_ignored = 0
        while self._current_char == '0':
            num_ignored += 1
            self._current_char = self._source.get()

        return num_ignored



    def construct_string_literal(self):

        if self._current_char != "\"":
            return False
        str_literal_value = ""
        self._current_char = self._source.get()
        while self._current_char != "\"":
            if self._current_char == BaseSource.EOF:
                raise ScannerException(self._token_position, "Missing closing \"")

            str_literal_value += str(self._current_char)
            self._current_char = self._source.get()

        self._token = Token(TokenType.STRING_LITERAL, value=str_literal_value, position=self._token_position)
        self._current_char = self._source.get()

        return True

    def construct_identifier(self):

        self._tmp_kw_id = ""
        self._tmp_len = 0
        if self.is_begin_valid():

            while self.is_valid_part() and self._tmp_len < Token.MAX_IDENTIFIER_LEN:

                self._tmp_kw_id += self._current_char
                self._tmp_len += 1
                self._current_char = self._source.get()

            if self.is_valid_part():
                # exceeded max length of the identifier
                raise ScannerException(self._token_position, "Exceeded max length of the identifier")

            if self.construct_keyword():
                return True

            self._token = Token(TokenType.IDENTIFIER, value=str(self._tmp_kw_id), position=self._token_position)
            return True

        else:
            return False



    def construct_keyword(self):

        try:
            tmp_token_type = self.kw_mapper.KEYWORD_MAP[self._tmp_kw_id]
            self._token = Token(tmp_token_type, value=str(self._tmp_kw_id), position=self._token_position)
            return True
        except:
            return False


    # ONLY for identifiers
    def is_begin_valid(self):
        # for keywords and identifiers
        if self._current_char.isalpha():
            self._tmp_kw_id += self._current_char
            self._current_char = self._source.get()
            self._tmp_len += 1
            return True
        # for identifiers only
        elif self._current_char in ["$", "_"]:
            self._tmp_kw_id += self._current_char
            self._current_char = self._source.get()
            if self._current_char.isalnum() or self._current_char == "_":
                self._tmp_kw_id += self._current_char
                self._current_char = self._source.get()
                self._tmp_len += 2
                return True

            else:
                raise ScannerException(self._source.get_position(), "Invalid Identifier")
        else:
            return False




    def is_valid_part(self):

        try:
            return self._current_char.isalnum() or self._current_char == "_"
        except Exception as e:
            print(e)

    def greetings(self):
        return "Just initialized a scanner class"