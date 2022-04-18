#Lista a posição que o valor se encontra em uma lista.

Lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print (Lista)
n = int(input('Digite um valor: '))
print("")
if n not in Lista:
    print("-1 O valor não existe.")
else:
    pos = Lista.index(n)
    print("O valor foi encontrado na posição: ", pos)
