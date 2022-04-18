def numerodevogaisPalavra(string):
    contador = 0

    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" \
        or char == "I" or char == "O" or char == "U":
            contador += 1

    return contador

def numerodeconsoantesPalavra(string):
    contador = 0

    for char in string:
        if char == "b" or char == "c" or char == "d" or char == "f" or char == "g" or char == "h" or char == "j" \
        or char == "k" or char == "l" or char == "m" or char == "n" or char == "p" or char == "q" or char == "r" \
        or char == "s" or char == "t" or char == "v" or char == "x" or char == "z" or char == "B" or char == "C" \
        or char == "B" or char == "C" or char == "D" or char == "F" or char == "G" or char == "H" or char == "J" \
        or char == "K" or char == "L" or char == "M" or char == "N" or char == "P" or char == "Q" or char == "R" \
        or char == "S" or char == "T" or char == "V" or char == "X" or char == "Z":

            contador += 1

    return contador

def numerodevogais(lista):
    contador = 0

    for palavra in lista:
        contador +=numerodevogaisPalavra(palavra)

    return contador

def numerodeconsoantes(lista):
    contador = 0

    for palavra in lista:
        contador +=numerodeconsoantesPalavra(palavra)

    return contador

palavras = input("Digite uma palavra: ").split()
print(numerodevogais(palavras))
print(numerodeconsoantes(palavras))