""" 1. Procedimento de leitura e Procedimento de Exibição """
def vetor():
    vetor = list(range(5))
    for i in vetor:
        n = int(input(f'valor{i+1}> '))
        vetor[i] = n
    print(vetor)

vetor()