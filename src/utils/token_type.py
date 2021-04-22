from enum import Enum, auto

class TokenType(Enum):

    IDENTIFIER =    auto()      #
    TYPE =          auto()      # "int", "string", "bool"

    PARENTHESIS_LEFT =  auto()   # "("
    PARENTHESIS_RIGHT = auto()  # ")"
    BRACKETS_LEFT =     auto()  # "["
    BRACKETS_RIGHT =    auto()  # "]"
    BRACES_LEFT =       auto()  # "{"
    BRACES_RIGHT =      auto()  # "}"

    COMMA =         auto()      # ","
    SEMICOLON =     auto()      # ";"
    MINUS =         auto()      # "-"
    PLUS =          auto()      # "+"
    MULTIPLY =      auto()      # "*"
    DIVIDE =        auto()      # "/"

    AND =           auto()      # "&&"
    OR =            auto()      # "||"

    GREATER =       auto()      # ">"
    LESS =          auto()      # "<"
    GREATER_EQUAL = auto()      # ">="
    LESS_EQUAL =    auto()      # "<="

    NOT =           auto()      # "!"
    EQUALS =        auto()      # "=="

    DEFINE =        auto()      # "define"

    FOREACH =       auto()      # "foreach"
    WHILE =         auto()      # "while"

    RETURN =        auto()      # "return"
    IF =            auto()      # "if"

    ELSE_IF =       auto()      # "else if"
    ELSE =          auto()      # else

    EOF =           auto()      # End of file
    UNDEFINED =     auto()      # Default/unknown token type