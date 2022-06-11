""" 15. Procedimento para realizar o cálculo solicitado (com parâmetro). """

def operacao(valor1, valor2, operacoes):

    if operacoes < 1 or operacoes >4 or operacoes == None:
        return 'operação não cadastrada!'

    if operacoes== 1:
        adicao= valor1 + valor2
        return f'o resultado da adição é {adicao}'

    if operacoes== 2:
        subtracao= valor1 - valor2
        return f'o resultado da subtração é {subtracao}'

    if operacoes== 3:
        divisao= valor1 / valor2
        return f'o resultado da divisão é {divisao}'

    if operacoes== 4:
        multiplicacao= valor1 * valor2
        return f'o resultado da multiplicação é {multiplicacao}'

print(operacao(5,5,1))#adição
print(operacao(5,5,2))#subtração
print(operacao(5,5,3))#divisão
print(operacao(5,5,4))#multiplicação
