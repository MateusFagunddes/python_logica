"""6.Dados dois vetores de 10 elementos, calcule o seu produto escalar. 
(O produto escalar de dois vetores v1 e v2 é dado 
por: produto = v1[0]*v2[0]+ v1[1]*v2[1]+... +v1[10]*v2[10])."""

vetor1 = [1,2,3,4,5,6,7,8,9,10]
vetor2 = [1,2,3,4,5,6,7,8,9,10]
vetor_escalar = list(range(10))
for i in range(0,10):
    vetor_escalar[i] = vetor1[i]*vetor2[i]
print(f'o produto escalar dos vetores é: {vetor_escalar}')
