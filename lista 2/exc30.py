""" Escreva um algoritmo que leia a idade de 2 homens e 2 mulheres 
(considere que a idade dos homens será sempre diferente, assim como das mulheres). 
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o 
produto das idades do homem mais novo com a mulher mais velha.  """

homem1 = int(input('Insira a idade do homem 1: '))
homem2 = int(input('Insira a idade do homem 2: '))
mulher1 = int(input('Insira a idade da mulher 1: '))
mulher2 = int(input('Insira a idade da mulher 2: '))

soma_idade= 0
produto_idade=0 

if homem1 > homem2:
    if mulher1 > mulher2:
        soma_idade = homem1 + mulher2
        produto_idade = homem2 * mulher1
       
    else:
        soma_idade = homem1 + mulher1
        produto_idade = homem2 * mulher2

else:
    if mulher1 > mulher2:
        soma_idade = homem1 + mulher2
        produto_idade = homem1 * mulher1
    else:
        soma_idade = homem1 + mulher1
        produto_idade = homem1 * mulher2

print(f'a soma das idades do homem mais velho com a mulher mais nova é {soma_idade}')
print(f'produto das idades do homem mais novo com a mulher mais velha é {produto_idade} ')
