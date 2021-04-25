from src.data_source.file_source import FileSource
from src.utils.token_type import TokenType
from src.scanner.scanner import Scanner
from src.utils.position import Position
from src.utils.position_source import PositionSource

import time

if __name__ == "__main__":

    print("Hello from the interpreter!")
    pos_file_source = PositionSource(
        FileSource("lang_codes/small_example.txt"),
        position=Position()
    )

    file_source1 = 1

    scanner = Scanner(pos_file_source)
    token = scanner.get_token()

    while True:
        print(token, "\n")

        if token.get_token_type() == TokenType.EOF:
            print("Hi there")
            break

        try:

            token = scanner.get_token()
        except Exception as e:
            print(e)
            breakpoint()
