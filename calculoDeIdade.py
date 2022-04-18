"""/ 5 - Calcular a idade dos filhos a partir da média de idade dos pais """

def calculaAltura(): 
    perguntaIMulher= int(input ("Mamãe, com que idade você teve seu bebê?\n ")); 
    alturaMulher = int (input("Qual sua altura em centímetros?\n "))
    perguntaIMarido = int (input("Papai, quantos anos você tinha quando seu filho nasceu?\n "));
    alturaHomem = int (input("Qual sua altura em centímetros?\n ")) 
    idade = int (input ("Seu filho já tem mais de 18 anos? Digite 1 para SIM e 0 para NÃO:\n "));

    mediaIdade = (perguntaIMulher + perguntaIMarido)/2; 
    mediaAltura = (alturaMulher + alturaHomem)/2;

    if (idade == 1): 
        if (mediaIdade < 30): 
            print(" Se for um menino, terá: ", mediaAltura + 10, "cm\n"); 
            print(" Se for uma menina, terá: ", mediaAltura - 9 , "cm\n");
        elif (mediaIdade >= 30): 
            print(" Se for um menino, terá: ", mediaAltura + 9 , "cm\n"); 
            print(" Se for uma menina, terá:", mediaAltura - 10 , "cm\n"); 
    elif(idade == 0): 
        print("Infelizmente sua criança ainda não tem idade o suficiente\n para completar o estudo!")

calculaAltura();
