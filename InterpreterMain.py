from src.data_source.file_source import FileSource
from src.scanner.scanner import Scanner
from src.utils.position import Position

if __name__ == "__main__":

    file_source = FileSource()
    scanner = Scanner(file_source)
    position = Position()

