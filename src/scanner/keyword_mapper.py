from ..utils.token_type import TokenType

class KeywordMapper():

    KEYWORD_MAP = {
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "else if": TokenType.ELSE_IF,
        "while": TokenType.WHILE,
        "foreach": TokenType.FOREACH,
        "return": TokenType.RETURN,
        "define": TokenType.DEFINE,
        "this": TokenType.THIS,
        "reflect": TokenType.REFLECT,
        "by_ref": TokenType.BY_REF,
        "true": TokenType.BOOL_LITERAL,
        "false": TokenType.BOOL_LITERAL
    }

    SINGLE_CHAR_MAP = {
        "(": TokenType.OPEN_PARENTHESIS,
        ")": TokenType.CLOSED_PARENTHESIS,
        "[": TokenType.OPEN_BRACKET,
        "]": TokenType.ClOSED_BRACKET,
        "{": TokenType.OPEN_CURLY_BRACKET,
        "}": TokenType.CLOSED_CURLY_BRACKET,
        ",": TokenType.COMMA,
        ";": TokenType.SEMICOLON,
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "*": TokenType.MULTIPLY,
        "/": TokenType.DIVIDE,
        "%": TokenType.MODULO
    }