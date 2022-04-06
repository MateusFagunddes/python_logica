""" Escrever um algoritmo que lê um número não determinado de mes
para m, todos inteiros e positivos, um de cada vez.
Se m for par, verificar quantos divisores possui e escrever esta informação.
Se m for ímpar e menor do que 10 calcular e escrever o contadorial de m.
Se m for ímpar e maior ou igual a 10 calcular e escrever a soma dos inteiros de 1 até m.  """

while True:
    valor = m = int(input('valor: '))
    contador = m

    if m % 2 == 0:
        divisoes = 0
        for i in range(m , 1-1, -1):
            if m % i == 0:
                divisoes +=1
        print(f'o numero {valor} é par e teve {divisoes} de 1 até ele mesmo!')

    if m % 2 != 0:
        fator = 1
        if m < 10:
            while contador >= 1:
                fator *= contador
                contador -= 1
            print(f'o fator de {m} é {fator}')
        else:
            for i in range(1, m,1):
                m+=i
            print(f'a soma dos numeros inteiros de 1 a {valor} é {m}')


