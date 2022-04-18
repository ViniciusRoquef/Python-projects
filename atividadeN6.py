import random; 
import math; 

numero = math.ceil(100 * random.random()); 
lim_inferior = 0; 
lim_superior = 100; 
contador = 0; 

while True:
    numeroUsuario = int(input("Digite um número qualquer, entre {} e {}: ". format(lim_inferior, lim_superior))); 
    if(numeroUsuario == numero): 
        contador += 1; 
        print("O numero de tentativas feitas foi de: {}". format(contador));
    elif(numeroUsuario > numero): 
        lim_superior = numero; 
        print("Digite um número qualquer, entre {} e {}: ". format(lim_inferior, lim_superior));
    else: 
        lim_inferior = numero 
        print("Digite um número qualquer, entre {} e {}: ". format(lim_inferior, lim_superior));



