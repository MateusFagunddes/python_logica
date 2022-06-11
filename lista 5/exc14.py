""" 3. Função que retorna a posição em que foi encontrado o valor. """


def encontrar(vetor, num_informado):
    if num_informado in vetor:
        return f'o índice de {num_informado} na lista informada é: {vetor.index(num_informado)}'
    else:
        return 'valor não encontrado!'

vetor_teste = [1,2,3,4,5,6,7,8,9,10]

print(encontrar(vetor_teste, 3))