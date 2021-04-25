from .base_source import BaseSource

class StringSource(BaseSource):


    def __init__(self, text):

        if text == "":
            raise Exception("No text provided")

        self.text = text
        self._current_position = 0
        if self._current_position >= len(self.text):
            self._current_char = BaseSource.EOF
        else:
            self._current_char = text[self._current_position]


    def get(self):

        temp_char = self._current_char
        self.next_char()
        return temp_char

    def next_char(self):

        self._current_position += 1
        if self._current_position < len(self.text):
            self._current_char = self.text[self._current_position]
        else:
            self._current_char = BaseSource.EOF
