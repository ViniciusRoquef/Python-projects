"""\ 2. Atividade:
2.1 Cadastro de um novo vendedor e o cálculo do salário de um vendedor. 
2.2 Cadastrar novo vendedor: Para proceder ao cadastro de um novo vendedor, o gerente deverá informar o  
nome, CPF e o setor de trabalho, sendo gerado e exibido ao final do cadastro um número de identificação(ID) do vendedor. 

-> Calcular salário do vendedor: A loja paga um salário fixo ao vendedor e dá uma comissão em porcentagem 
sobre o total de vendas (em reais) efetuadas por ele no mês, sendo 3% para até R$ 5.000,00 em vendas; 
6% para vendas acima de R$ 5.000,00 e até R$ 10.000,00; e 10% para valores acima de R$ 10.000,00 em 
vendas. O salário final é calculado somando-se o salário fixo mais a comissão recebida. Ao final do 
cálculo, informar na tela o  nome do vendedor e o salário que deverá receber ao fim do mês. """ 

import random
IdVendedor = random.random()
vendedor = input('Novo cadastro: '); 
cpf = int(input('Nº do CPF: ')); 
novoSetor = input ('Setor de trabalho: '); 
salarioBase = 1000; # Salario base = 1.000 reais 
totalDeVendas = int(input("Quantos produtos você vendeu este mês?")); 

if (totalDeVendas > 0 ) and (totalDeVendas <= 5000): 
    print('O nome do Cliente é: ', vendedor, '\nCPF :', cpf, '\nSetor de trabalho: ', novoSetor,)
    print('Seu código de identificação é: ', IdVendedor)
    print('Seu salário este mês + comissão mensal é: ', (0.03 * 1000) + salarioBase, 'reais' ); 
elif (totalDeVendas >= 5001 ) and ( totalDeVendas <= 10000): 
    print('O nome do Cliente é: ', vendedor, '\nCPF :', cpf, '\nSetor de trabalho: ', novoSetor)
    print('Seu código de identificação é: ', IdVendedor)
    print('Seu salário este mês + comissão mensal é: ', (0.06 * 1000) + salarioBase, 'reais' ); 
elif totalDeVendas > 10000: 
    print('O nome do Cliente é: ', vendedor, '\nCPF :', cpf, '\nSetor de trabalho: ', novoSetor)
    print('Seu código de identificação é: ', IdVendedor)
    print('Seu salário este mês + comissão mensal é: ', (0.10 * 1000) + salarioBase, 'reais' ); 
else: 
    print ('Desculpe, se você não vendeu nada, não terá acréscimo comissional este mês'); 
exit(); 

