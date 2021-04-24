from src.data_source.file_source import FileSource
from src.scanner.scanner import Scanner
from src.utils.position import Position


if __name__ == "__main__":

    print("Hello from the interpreter!")
    file_source = FileSource("lang_codes/small_example.txt")
    file_source1 = 1
    scanner = Scanner(file_source)
    scanner.get_text()

    position = Position()