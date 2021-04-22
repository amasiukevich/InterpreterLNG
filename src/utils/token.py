from .token_type import TokenType
from .position import Position


class Token:

    def __init__(self, token_type: TokenType, position: Position):

        self.type = token_type
        self.position = position



    # for testing purposes
    def __repr__(self):
        return f"TOKEN(type: {self.token_type}"