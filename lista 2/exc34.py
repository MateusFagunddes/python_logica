""" O banco GASTADOR Ltda. deseja utilizar o computador para determinar 
o limite da conta especial de seus clientes a partir do saldo da 
conta corrente e da poupança. Escreva um algoritmo para ler o saldo 
da conta corrente e da poupança de um cliente e Escreva o seguinte: 

a. A mensagem: ‘SEM CONTA ESPECIAL’ Se o cliente NÃO possuir o 
requisito necessário para a conta especial. 
(REQUISITO PARA POSSUIR CONTA ESPECIAL: o saldo em pelo menos 
uma das duas contas deve estar acima de R$1.000,00) 

b. O valor do limite da conta conforme especificação abaixo:  
O valor limite da conta especial  fornecido ao cliente deve ser 
o dobro do maior saldo (entre conta corrente e poupança) ou o 
triplo do menor saldo. Deve ser fornecido o valor de limite maior 
entre essas 2 situações.  """


conta_corrente = float(input('insira o saldo da conta corrente: '))
conta_poupança = float(input('insira o saldo da conta poupança: '))
maiorSaldo=0
menorSaldo=0
limiteEspecial = 0


if conta_corrente >= 1000 or conta_poupança >= 1000:
    if conta_corrente > conta_poupança:
        maiorSaldo = conta_corrente
        menorSaldo = conta_poupança
    else:
        maiorSaldo = conta_poupança
        menorSaldo = conta_corrente
        
    calculo_pou= maiorSaldo *2
    calculo_cor= menorSaldo*3

    if calculo_pou > calculo_cor:
        limiteEspecial = calculo_pou
        print(f'O limite da conta especial é R${limiteEspecial}')
    else:
        limiteEspecial = calculo_cor
        print(f'O limite da conta especial é R${limiteEspecial}')
else:
    print('SEM CONTA ESPECIAL')