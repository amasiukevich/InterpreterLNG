from .base_source import BaseSource


import io
"""
    Author: Anton Masiukevich
    Github: https://github.com/amasiukevich

    Scanner class implements a scanner for the text of the file
"""

class FileSource(BaseSource):

    def __init__(self, filename: str):
        self.filename = filename
        self.reader = io.open(self.filename, "r")
        self.character = self.reader.read(1)

    def peek(self):
        return self.character

    def get(self):
        temp_char = self.character
        self.next()
        return temp_char

    def next(self):
        self.character = self.reader.read(1)
        if not self.character:
            self.character = BaseSource.EOF

    def greetings(self):
        return "Hello from the FileSource"