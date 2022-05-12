""" 7.	Leia 2 vetores com 10 elementos cada. Considerando cada 
vetor como sendo um conjunto, crie um terceiro vetor, que seja 
a união dos dois primeiros, e um quarto, que seja a intersecção 
entre os dois primeiros. """

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
vetor3 = []
vetor4 = []

for i in range(0,10):
    vetor3.append(vetor1[i])
for i in range(0,10):    
    vetor3.append(vetor2[i])   
for i in range(0,10):
    if vetor1[i] in vetor2:
        vetor4.append(vetor1[i])

print(f'o vetor1 é: {vetor1}\n')
print(f'o vetor2 é: {vetor2}\n')
print(f'o vetor3 é: {vetor3}\n')
print(f'os valores que constam em ambos os vetores são: {vetor4}')

