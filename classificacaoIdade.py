"""\ 1. Elabore um algoritmo que chama uma função que recebe uma idade de um nadador e classifica-o 
em uma das  seguintes categorias: 
∙ Infantil = 5 - 10 anos 
∙ Juvenil = 11-17 anos  
∙ Adulto = 18-25 anos """

idade = int(input (' Digite sua idade atleta: ')); 
print(idade); 
if (idade >= 5) and (idade <=10): 
    print('Categoria infantil'); 
elif (idade>=11) and (idade <=17): 
    print('Categoria Juvenil'); 
elif (idade >= 18) and (idade <= 25): 
    print ('Categoria Adulto'); 
else: 
    print ('Desculpe, só aceitamos participantes com idades entre 5 à 25 anos!');
exit();

