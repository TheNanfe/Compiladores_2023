class Lexer:

    def __init__(self, whole_json, current_position=0):
        self.whole_json = whole_json
        self.positions_to_skip = 0
        self.current_position = current_position
        self.to_parse = ''
        self.tokens = []

    def is_string(self):

        self.positions_to_skip = 0
        string_to_parse = self.whole_json[self.current_position - 1:]
        string_characters = []

        for character in string_to_parse:

            string_characters.append(character)

            if self.positions_to_skip == 0:
                if character != '"':
                    return False

            elif character == '"':
                self.current_position += self.positions_to_skip
                return True

            self.positions_to_skip += 1

        raise Exception('String mal formado. El String debe terminar con una comilla doble.')

    def is_null(self):
        return self.verify_operator('null', 4)

    def is_false(self):
        return self.verify_operator('false', 5)

    def is_true(self):
        return self.verify_operator('true', 4)

    def verify_operator(self, operator, number_characters):

        self.positions_to_skip = 0

        string_to_parse = self.whole_json[self.current_position - 1:]
        string_characters = []

        for character in string_to_parse:

            string_characters.append(character)

            if len(string_characters) == number_characters:
                if ''.join(string_characters).lower() == operator:
                    self.current_position += self.positions_to_skip
                    return True
                else:
                    return False

            self.positions_to_skip += 1

    def get_token(self):

        self.current_position += 1

        if self.to_parse == ' ':
            return 'NO_TOKEN'
        elif self.to_parse == '[':
            return 'L_CORCHETE'
        elif self.to_parse == ']':
            return 'R_CORCHETE'
        elif self.to_parse == '{':
            return 'L_LLAVE'
        elif self.to_parse == '}':
            return 'R_LLAVE'
        elif self.to_parse == ',':
            return 'COMA'
        elif self.to_parse == ':':
            return 'DOS_PUNTOS'
        elif self.to_parse == 'number':
            return 'number'
        elif self.is_string():
            return 'LITERAL_CADENA'
        elif self.is_null():
            return 'PR_NULL'
        elif self.is_false():
            return 'PR_FALSE'
        elif self.is_true():
            return 'PR_TRUE'
        elif self.to_parse == 'eof':
            return 'eof'
        else:
            raise Exception('No existe ese simbolo en el lenguaje')

    def tokenize(self):
        for token in self.whole_json:
            if self.positions_to_skip == 0:
                self.to_parse = token
                self.tokens.append(self.get_token())
                print(self.tokens)
            else:
                self.positions_to_skip -= 1


a = Lexer('{"name":"John", "car":false, "car":true, "car":null}')
a.tokenize()
