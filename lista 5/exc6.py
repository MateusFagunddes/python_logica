""" 15. Procedimento para realizar o cálculo solicitado (com parâmetro). """

def operacao(valor1, valor2, operacoes):
    if operacoes < 1 or operacoes >4 or operacoes == None:
        print('operação não cadastrada!')

    if operacoes== 1:
        adicao= valor1 + valor2
        print(f'o resultado da adição é {adicao}')

    if operacoes== 2:
        subtracao= valor1 - valor2
        print(f'o resultado da subtracao é {subtracao}')

    if operacoes== 3:
        divisao= valor1 / valor2
        print(f'o resultado da divisao é {divisao}')

    if operacoes== 4:
        multiplicacao= valor1 * valor2
        print(f'o resultado da multiplicacao é {multiplicacao}')

operacao(5,5,1)
operacao(5,5,2)
operacao(5,5,3)
operacao(5,5,4)
