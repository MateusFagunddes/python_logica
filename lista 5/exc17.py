""" 9. Procedimento que atualiza e/ou inclui o número no vetor 
de elementos se o número já foi encontrado ou não. """
import numpy as np

def contaValor(matriz):
    print(matriz, '\n')
    contador = {}
    for l in matriz:
        for c in l:
            if np.sum(matriz==c)>1:
                contador[c] = np.sum(matriz==c)
    for numero in contador:
        qtd = contador[numero]
        print(f'o valor {numero} repetiu {qtd}', end= ', ')
    print('\n')


matriz_teste = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35],[36,37,38,39,40],[41,42,43,44,45],[1,2,3,4,5]])
contaValor(matriz_teste)