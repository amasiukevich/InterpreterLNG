from ..utils.position import Position

class ScannerException(Exception):

    def __init__(self, position: Position, msg: str):
        super().__init__(f"Scanner exception at position {position}: {msg}")