"""/ 4. Elabore um algoritmo que simule a tela de login de um aplicativo (como mostrado na Figura 2). 
O usuário deverá  fornecer nome de Usuário e Senha. Caso o usuário erre o login 4 vezes, deverá ser 
bloqueado (Exibir mensagem).  """ 

loginFuncionarios = {}; 
def add_funcionario (codigo, nome): 
    loginFuncionarios.update({codigo : nome})

resposta = 0; 
while resposta != '2':
    print('[ 1 ] Cadastro usuário '); 
    print('[ 2 ] Sair da aplicação ');
    
    resposta = int (input ('Escolha uma das opções: ')); 

    if (resposta == 1 ):
        contador = 0
        user = 'admin'
        password = 'admin123'

        while contador <= 4: 
            usuarioAcess = input("Qual o seu nome de usuário? "); 
            senhaAcess = input("Digite uma senha? ");

            if usuarioAcess == user and senhaAcess == password: 
                print("Login efetuado!\n"); 
            elif usuarioAcess != user or senhaAcess != password: 
                print("Acesso negado! Por favor verifique suas credenciais.\n"); 
                contador +=1 
            elif contador == 4: 
                print("Usuário bloqueado, por favor procure ajuda com os provedores!");
                exit(); 

    












