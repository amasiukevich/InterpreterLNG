class Position:

    def __init__(self, line=1, column=0):
        self._line = line
        self._column = column

    def get_line(self):
        return self._line

    def get_column(self):
        return self._column

    def advance_line(self):
        self._line += 1
        self.column = 0

    def advance_column(self):
        self.column += 1

    def __repr__(self):
        return f"line: {self.get_line()}, column: {self.get_column()}"

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        else:
            return self.get_line() == other.get_line() and self.get_column() == other.get_column()


    def clone(self):
        return Position(line=self.get_line(), column=self.get_column())

    def greetings(self):
        return "Hello from the Position"