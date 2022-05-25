def lexica(codigo):
    codigo += " "
    estado = 0
    i = 0
    line = 0
    # Lista de token
    tokens = []
    # Tabela de simbolos
    symbols = ['adicionar tabela de simbolos']
    identifiers = []
    reservedwords = [
        'int', 'float', 'char', 'boolean',
        'void', 'if', 'else', 'for',
        'while', 'scanf', 'println',
        'main', 'return']
    tokenstart = 0
    lineindex = 0
    tokenindex = 0
    
    # Encontra um indice de um identificador de nome
    def find(value):
        for i, dic in enumerate(identifiers):
            if dic['name'] == value:
                return i
        return -1
    
    while i < len(codigo):
        if codigo[i] == "\n":
            line = line + 1
            lineindex = i + 1 >= len(codigo) if 0 else i + 1
        # Estado inicial
        if estado == 0:
            if codigo[i].isalpha():
                estado = 1
                i += 1
            elif codigo[i].isnumeric():
                estado = 3
                i += 1
            elif codigo[i] == '"':
                estado = 8
                i += 1
            elif codigo[i] == '/':
                estado = 10
                i += 1
            elif codigo[i] == '+':
                estado = 14
                i += 1
            elif codigo[i] == '-':
                estado = 15
                i += 1
            elif codigo[i] == '*':
                estado = 16
                i += 1
            elif codigo[i] == '%':
                estado = 17
                i += 1
            elif codigo[i] == '=':
                estado = 18
                i += 1
            elif codigo[i] == '!':
                estado = 21
                i += 1
            elif codigo[i] == '>':
                estado = 24
                i += 1
            elif codigo[i] == '<':
                estado = 27
                i += 1
            elif codigo[i] == '|':
                estado = 30
                i += 1
            elif codigo[i] == '&':
                estado = 32
                i += 1
            elif codigo[i] == ',':
                estado = 34
                i += 1
            elif codigo[i] == ';':
                estado = 35
                i += 1
            elif codigo[i] == '(':
                estado = 36
                i += 1
            elif codigo[i] == ')':
                estado = 37
                i += 1
            elif codigo[i] == '[':
                estado = 38
                i += 1
            elif codigo[i] == ']':
                estado = 39
                i += 1
            elif codigo[i] == '{':
                estado = 40
                i += 1
            elif codigo[i] == '}':
                estado = 41
                i += 1
            elif codigo[i] in (' ', '\n', '\r', '\r\n', '\t'):
                estado = 0
                i += 1
            else:
                estado = 42
                i += 1
            tokenstart = i

        # Caso de qualquer letra ou numero
        elif estado == 1:
            if codigo[i].isalnum() and codigo[i] != ' ':
                estado = 1
                i += 1
            else:
                estado = 2

        # Estado final para id ou palavra reservada
        elif estado == 2:
            v = codigo[tokenstart-1:i]
            if v in reservedwords:
                t = v.upper()
            else:
                # procura o indice do meu id na lista
                idindex = find(v)
                # Caso haja encontrado o usa
                if idindex>=0:
                    t = f'ID:{idindex}'
                else:
                    t = f'ID:{tokenindex}'
                    identifiers.append({'id':tokenindex,'name':v})
                    tokenindex += 1
               
            tokens.append((t, v))
            estado = 0

        # Estado para numerico int ou decimal
        elif estado == 3:
            if codigo[i].isnumeric():
                estado = 3
                i += 1
            elif codigo[i] == '.':
                estado = 5
                i += 1
            else:
                estado = 4

        # Estado final de numerico int
        elif estado == 4:
            tokens.append(("NUMINT", codigo[tokenstart-1:i]))
            estado = 0

        # Estado para numero decimal
        elif estado == 5:
            if codigo[i].isnumeric():
                estado = 6
                i += 1
            else:
                estado = 42
        elif estado == 6:
            if codigo[i].isnumeric():
                estado = 6
                i += 1
            else:
                estado = 7

        # Estado final de numero decimal
        elif estado == 7:
            tokens.append(("NUMDEC", codigo[tokenstart-1:i]))
            estado = 0
            i += 1

        # Estado para literal
        elif estado == 8:
            if codigo[i] == '"':
                estado = 9
                # i += 1
            elif codigo[i] == '\n':
                estado = 42
                i += 1
            else:
                estado = 8
                i += 1

        # Estado final para literal
        elif estado == 9:
            tokens.append(("TEXTO", codigo[tokenstart-1:i]))
            estado = 0
            i += 1

        # Estado para barra ou comentario
        elif estado == 10:
            if codigo[i] == '/':
                estado = 11
                i += 1
            else:
                estado = 13

        # Estado para comentarios
        elif estado == 11:
            if codigo[i] == "\n":
                estado = 12
            else:
                i += 1

        # Estado final de comentarios
        elif estado == 12:
            estado = 0
            i += 1

        # Estado final para barra
        elif estado == 13:
            tokens.append(("/", "/"))
            estado = 0

        # Estado final +
        elif estado == 14:
            tokens.append(("+", "+"))
            estado = 0

        # Estado final -
        elif estado == 15:
            tokens.append(("-", "-"))
            estado = 0

        # Estado final *
        elif estado == 16:
            tokens.append(("*", "*"))
            estado = 0
            

        # Estado final %
        elif estado == 17:
            tokens.append(("%", "%"))
            estado = 0
            

        # Estado do comparação ou atribuição
        elif estado == 18:
            if codigo[i] == '=':
                estado = 19
            else:
                estado = 20

        # Estado final comparação ==
        elif estado == 19:
            tokens.append(("COMP", "=="))
            estado = 0
            i += 1

        # Estado final atribuição
        elif estado == 20:
            tokens.append(("=", "="))
            estado = 0

        # Estado negação ou comparação
        elif estado == 21:
            if codigo[i] == '=':
                estado = 22
            else:
                estado = 23

        # Estado final comparação !=
        elif estado == 22:
            tokens.append(("COMP", "!="))
            estado = 0
            i += 1

        # Estado final negação
        elif estado == 23:
            tokens.append(("!", "!"))
            estado = 0

        # Estado maior ou comparação >=
        elif estado == 24:
            if codigo[i] == '=':
                estado = 25
            else:
                estado = 26

        # Estado final comparação >=
        elif estado == 25:
            tokens.append(("COMP", '>='))
            estado = 0
            i += 1

        # Estado final maior
        elif estado == 26:
            tokens.append(("COMP",">"))
            estado = 0

        # Estado menor ou comparação <=
        elif estado == 27:
            if codigo[i] == '=':
                estado = 28
            else:
                estado = 29

        # Estado final comparação <=
        elif estado == 28:
            tokens.append(("COMP", "<="))
            estado = 0
            i += 1

        # Estado final menor
        elif estado == 29:
            tokens.append(("COMP", "<"))
            estado = 0

        # Estado operador ou
        elif estado == 30:
            if codigo[i] == '|':
                estado = 31
            else:
                estado = 42

        # Estado final operador ou
        elif estado == 31:
            tokens.append(("||", "||"))
            estado = 0
            i += 1
        elif estado == 32:
            if codigo[i] == '&':
                estado = 33
            else:
                estado = 42

        # Estado final operador e
        elif estado == 33:
            tokens.append(("&&", "&&"))
            estado = 0
            i += 1

        # Estado final virgula
        elif estado == 34:
            tokens.append((",", codigo[i-1]))
            estado = 0

        # Estado final ponto-virgula
        elif estado == 35:
            tokens.append((";", codigo[i-1]))
            estado = 0

        # Estado final abre parenteses
        elif estado == 36:
            tokens.append(("(", codigo[i-1]))
            estado = 0

        # Estado final fecha parenteses
        elif estado == 37:
            tokens.append((")", codigo[i-1]))
            estado = 0

        # Estado final abre colchetes
        elif estado == 38:
            tokens.append(("[", codigo[i-1]))
            estado = 0

        # Estado final fecha colchetes
        elif estado == 39:
            tokens.append(("]", codigo[i-1]))
            estado = 0

        # Estado final abre chaves
        elif estado == 40:
            tokens.append(("{", codigo[i-1]))
            estado = 0

        # Estado final fecha chaves
        elif estado == 41:
            tokens.append(("}", codigo[i-1]))
            estado = 0

        # Estado final erro
        elif estado == 42:
            # Procura a proxima quebra de linha para obter a
            # linha completa do erro
            errorline = ""
            x = lineindex
            while(x < len(codigo)):
                if codigo[x] == '\n' or x == len(codigo)-1:
                    if x == len(codigo)-1:
                        errorline = codigo[lineindex:]
                    else:
                        errorline = codigo[lineindex:x]
                    break
                x += 1

            # Retorna a mensagem de erro
            return f"Erro de compilação na linha {line}\n erro:{errorline}"
    return tokens


if __name__ == '__main__':
    print(lexica('''[a(a)a{a}a]'''))