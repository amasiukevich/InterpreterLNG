from src.scanner.scanner import Scanner
from src.utils.position_source import PositionSource
from src.data_source.string_source import StringSource
from src.utils.position import Position
from src.utils.token import Token
from src.utils.token_type import TokenType

from src.utils.accumulator import accumulate_tokens

import unittest


class TestScanner(unittest.TestCase):

    def test_brackets(self):

        scanner = Scanner(
            PositionSource(
                StringSource("{()}"),
                Position()
            )
        )
        tokens = accumulate_tokens(scanner)

        self.assertListEqual(
            tokens, [
                Token(TokenType.OPEN_CURLY_BRACKET, Position(1, 1), value="{"),
                Token(TokenType.OPEN_PARENTHESIS, Position(1, 2), value="("),
                Token(TokenType.CLOSED_PARENTHESIS, Position(1, 3), value=")"),
                Token(TokenType.CLOSED_CURLY_BRACKET, Position(1, 4), value="}")
            ]
        )

    def test_function_definition(self):

        scanner = Scanner(
            PositionSource(
                StringSource("define factorial(n) {}"),
                Position()
            )
        )

        tokens = accumulate_tokens(scanner)


        self.assertListEqual(
            tokens, [
                Token(TokenType.DEFINE, Position(1, 1), value="define"),
                Token(TokenType.IDENTIFIER, Position(1, 8), value="factorial"),
                Token(TokenType.OPEN_PARENTHESIS, Position(1, 17), value="("),
                Token(TokenType.IDENTIFIER, Position(1, 18), value="n"),
                Token(TokenType.CLOSED_PARENTHESIS, Position(1, 19), value=")"),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(1, 21), value="{"),
                Token(TokenType.CLOSED_CURLY_BRACKET, Position(1, 22), value="}")
            ]
        )


    def test_arithmetic(self):


        scanner = Scanner(
            PositionSource(
                StringSource("a = 10000;"),
                Position()
            )
        )

        tokens = accumulate_tokens(scanner)

        self.assertListEqual(
            tokens, [
                Token(TokenType.IDENTIFIER, Position(1, 1), value="a"),
                Token(TokenType.ASSIGN, Position(1, 3), value="="),
                Token(TokenType.NUMERIC_LITERAL, Position(1, 5), value="10000"),
                Token(TokenType.SEMICOLON, Position(1, 10), value=";")
            ]
        )

