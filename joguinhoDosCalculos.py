"""/ 7. Faça um joguinho para testar os conhecimentos de adição e subtração. O jogo deve gerar dois 
números inteiros aleatoriamente e um operador de adição ou subtração também aleatoriamente e perguntar
ao usuário o resultado da operação. Se o usuário acertar, exibir a mensagem de acerto, caso contrário, 
exibir mensagem de erro. O jogo termina se o usuário errar 4 vezes, perdendo o jogo, ou quando fizer 
dez acertos consecutivos, ganhando o jogo."""

import random
from sre_constants import error;
import math;

resposta = 0; 
while resposta != '2':
    print('[ 1 ] JOGAR: '); 
    print('[ 2 ] Não quero jogar: ');

    resposta = int (input('Escolha uma das opções: ')); 
    
    if (resposta == 1):
        print ("\n\n###########################################");
        print ("######## JOGUINHO DOS CÁLCULOS ############"); 
        print ("###########################################\n\n"); 
        print ("Regras do jogo: erre 4 vezes o cálculo proposto e perca,\nou acerte 10 vezes consecutivas e ganhe :)");
        print ("Vamos começar!\n\n")
    elif(resposta == 2): 
        print ("Que pena :( \n Esperamos você na próxima!")
    break;

def geraCalculo(): 
    numero1 = math.ceil(100 * random.random()); 
    numero2 = math.ceil(100 * random.random()); 
    sinal = random.choice(["-","+"]); 

    if (sinal == "+"):
        a = numero1 + numero2 
        print(numero1, "+" ,numero2, "=" );
        resultado = int(input("Qual é o resultado da adição? ")); 
        if (resultado != a): 
            print("Você errou :(");
            return False;
        elif (resultado == a): 
            print("Acertou, parabéns!");
            return True;

    elif(sinal == "-"):
        b = numero1 - numero2 
        print(numero1 ,"-", numero2, "=" );
        resultado = int(input("Qual é o resultado da adição? "));
        if (resultado != b): 
            print("Você errou :(");
            return False;
        elif (resultado == b): 
            print("Acertou, parabéns!");
            return True;

acertos = 0; 
erros = 0; 

while acertos <=10 or erros <= 4: 
    geraCalculo(); 
    acertos += 1 
    erros +=1
    if acertos == 10:
        print(" -------------------------------");
        print("|  Parabéns, você venceu o jogo |");
        print(" -------------------------------")
        break;
    elif erros == 4: 
        print(" -------------------------------");
        print("|   Desculpe, você perdeu! :(   |");
        print(" -------------------------------")
        break;





    

