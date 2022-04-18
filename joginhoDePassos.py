"""/3- Faça um joguinho para crianças que consiste em pedir ao usuário quantos passos um gatinho deve dar 
e de  quantos em quantos passos o gato deve miar. Escrever na tela o número de cada passo dado pelo ga- 
to e o miado.  """

# Laço com variável de controle
passos = int(input('Quantos passos o gatinho vai dar? ')); 
miar = int(input('De quantos em quantos passos o gatinho vai miar?: ')); 
qtdMiados = int(passos/miar);
qtdPassos = passos - qtdMiados;

for qtdPassos in range (0, passos+1, miar):
    print(qtdPassos,"\n");
    print("Miauuuuuu\n")
print('A quantidade de passos dados é: ', qtdPassos, 'e a quantidade de miados é: ', qtdMiados);



