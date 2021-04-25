from src.utils.token_type import TokenType

def accumulate_tokens(scanner):

    tokens = []
    token = scanner.get_token()

    while token.get_token_type() != TokenType.EOF:

        tokens.append(token)
        try:
            token = scanner.get_token()
        except Exception as e:
            print(e)

    return tokens