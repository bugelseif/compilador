def lexica(codigo):
    estado = 0
    i = 0

    while i < len(codigo):
        if estado == 0:
            if codigo[i].isalpha():
                estado = 1
                print(f'alfa {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i].isnumeric():
                estado = 3
                print(f'num {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '"':
                estado = 8
                print(f' " {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '/':
                estado = 10
                print(f' / {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '+':
                estado = 14
                print(f' + {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '-':
                estado = 15
                print(f' - {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '*':
                estado = 16
                print(f' * {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '%':
                estado = 17
                print(f' % {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '=':
                estado = 18
                print(f' = {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '!':
                estado = 21
                print(f' ! {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '>':
                estado = 24
                print(f' > {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '<':
                estado = 27
                print(f' < {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '|':
                estado = 30
                print(f' | {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '&':
                estado = 32
                print(f' & {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == ',':
                estado = 34
                print(f' , {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == ';':
                estado = 35
                print(f' ; {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '(':
                estado = 36
                print(f' ( {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == ')':
                estado = 37
                print(f' ) {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '[':
                estado = 38
                print(f' [ {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == ']':
                estado = 39
                print(f' ] {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '{':
                estado = 40
                print(f' chave {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == '}':
                estado = 41
                print(f' chave {codigo[i]}, estado {estado}')
                i += 1
            elif codigo[i] == ' ':
                estado = 0
                print(f' vazio {codigo[i]}, estado {estado}')
                i += 1
            else:
                estado = 42
                i += 1
                print(f' erro {codigo[i]}, estado {estado}')            
        elif estado == 1:
            if codigo[i].isalnum():
                estado = 1
                print(f'alfanum {codigo[i]}, estado {estado}')
                i += 1
            else:
                estado = 2
                i += 1
        elif estado == 2:
            ...
            i += 1
        elif estado == 3:
            if codigo[i].isnumeric():
                estado = 3
                i += 1
            elif codigo[i] == '.':
                estado = 5
                i += 1
            else:
                estado = 4
        elif estado == 4:
            ...
            i += 1
        elif estado == 5:
            if codigo[i].isnumeric():
                estado = 6
                i += 1
            else:
                estado = 42
                i += 1
        elif estado == 6:
            ...
            i += 1


if __name__ == '__main__':
    print(lexica('"/teste1 $ 23%{-- 5|'))
