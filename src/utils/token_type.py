from enum import Enum, auto

class TokenType(Enum):


    IDENTIFIER = auto(),
    COMMENT = auto(),           # "#"

    # Logical operators
    AND = auto(),               # &&
    OR = auto(),                # ||
    NOT = auto(),               # !

    # Relational
    ASSIGN = auto(),            # =
    EQUAL = auto(),             # ==
    NOT_EQUAL = auto(),         # !
    GREATER = auto(),           # >
    LESS = auto(),              # <
    GREATER_EQUAL = auto(),     # >=
    LESS_EQUAL = auto(),        # <=

    # Arithmetical operators
    PLUS = auto(),              # +
    MINUS = auto(),             # -
    MULTIPLY = auto(),          # -
    DIVIDE = auto(),            # /
    MODULO = auto(),            # %

    # default keywords
    IF = auto(),                # if
    ELSE_IF = auto(),           # else if
    ELSE = auto(),              # else
    WHILE = auto(),             # while
    FOREACH = auto(),           # foreach
    RETURN = auto(),            # return
    DEFINE = auto(),            # define
    THIS = auto(),              # this
    REFLECT = auto(),           # reflect
    BY_REF = auto(),            # by_ref

    # Symbols
    OPEN_PARENTHESIS = auto(),      # (
    CLOSED_PARENTHESIS = auto(),    # )
    OPEN_BRACKET = auto(),          # [
    ClOSED_BRACKET = auto(),        # ]
    OPEN_CURLY_BRACKET = auto(),    # {
    CLOSED_CURLY_BRACKET = auto(),  # }
    COMMA = auto(),                 # ,
    SEMICOLON = auto(),             # ;

    # Literals
    NUMERIC_LITERAL = auto(),       # 123
    STRING_LITERAL = auto(),        # abcde
    BOOL_LITERAL = auto(),          # true, false

    UNKNOWN = auto(),
    EOF = auto()


    IDENTIFIER =    auto()      #
    TYPE =          auto()      # "int", "string", "bool"