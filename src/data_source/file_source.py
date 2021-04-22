from .base_source import BaseSource
"""
    Author: Anton Masiukevich
    Github: https://github.com/amasiukevich

    Scanner class implements a scanner for the text of the file
"""

class FileSource(BaseSource):

    def __init__(self):
        self.greetings()

    def peek(self):
        pass

    def get(self):
        pass

    def greetings(self):
        return "Hello from the FileSource"