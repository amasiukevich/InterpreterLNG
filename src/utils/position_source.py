from ..data_source.base_source import BaseSource
from .position import Position

class PositionSource(BaseSource):


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
            self._position.advance_column()


    def get_line(self):
        return self._position.get_line()


    def get_column(self):
        return self._position.get_column()


    def get_position(self):
        return self._position.clone()