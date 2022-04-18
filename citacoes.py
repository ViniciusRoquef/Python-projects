# Algoritmo que pega o seu ultimo nome, e coloca inicialmente -> Usado para citações

n = str(input('Digite o seu nome completo:')).strip()
nome = n.split()
sobrenome = nome.pop()
print(sobrenome + ", " + " ".join(nome))