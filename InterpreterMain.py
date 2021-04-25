from src.data_source.file_source import FileSource
from src.utils.token_type import TokenType
from src.scanner.scanner import Scanner
from src.utils.position import Position
from src.utils.position_source import PositionSource

from src.utils.accumulator import accumulate_tokens

import time

if __name__ == "__main__":

    print("Hello from the interpreter!")
    pos_file_source = PositionSource(
        FileSource("lang_codes/small_example.txt"),
        position=Position()
    )

    file_source1 = 1

    scanner = Scanner(pos_file_source)

    tokens = accumulate_tokens(scanner)

    breakpoint()