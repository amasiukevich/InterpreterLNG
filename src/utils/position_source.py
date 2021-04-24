from ..data_source.base_source import BaseSource
from .position import Position

class PositionSource:


    def __init__(self, source: BaseSource, position: Position):
        self._source = source
        self._position = position


    def get(self):
        character = self._source.get()
        self.advance(character)
        return character


    def advance(self, character):
        if character == "\n":
            self._position.advance_line()
        else:
            self.position.advance_line()


    def get_line(self):
        return self.position.get_line()


    def get_column(self):
        return self.position.get_column()


    def get_position(self):
        return self.position.clone()