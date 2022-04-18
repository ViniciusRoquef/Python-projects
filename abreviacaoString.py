#Algoritmo que abrevia seu último nome, e coloca-o inicialmente precedido de .

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
sobrenome = nome.pop()
print(sobrenome[0] + ". " + " ".join(nome))