#Contador de palavras em uma frase.

frase = str(input('Digite uma frase: ')).strip()
palavra = str(input('Digite uma palavra: '))
print('A palavra aparece {} vezes na frase'.format(frase.count(palavra)))
