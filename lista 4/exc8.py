""" 8.	Leia duas matrizes de dimensões 3 X 3 e
 em seguida calcule seu produto. """

matriz1 = [[2,2,2], [2,2,2], [2,2,2]]
matriz2 = [[4,4,4], [6,6,6], [8,8,8]]
soma_matriz = [[0,0,0,],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        soma_matriz[l][c] = matriz1[l][c] * matriz2[l][c] 

print(soma_matriz)