""" 1.	Solicite ao usuário 5 números inteiros, guarde-os 
em um vetor e em seguida imprima-os na tela.  """

vetor = list(range(5))

for i in vetor:
    n = int(input('> '))
    vetor[i] = n
print(vetor)
