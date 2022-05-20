""" 8. Procedimento que calcule o produto dos vetores e 
Procedimento para exibição do vetor do produto. """

def multiMatriz(matriz1, matriz2):
    #importei o numpy pra mostrar a matriz formatada
    import numpy as np
    produto_matriz = np.array([[0,0,0,],[0,0,0],[0,0,0]])
    for l in range(0,3):
        for c in range (0,3):
            produto_matriz[l][c] = matriz1[l][c] * matriz2[l][c] 
    print(produto_matriz)


matriz_teste1 = [[1,2,3],[4,5,6],[7,8,9]]
matriz_teste2 = [[2,2,2],[2,2,2],[2,2,2]]
multiMatriz(matriz_teste1,matriz_teste2)