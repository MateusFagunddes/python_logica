""" Foi feita uma pesquisa entre os habitantes de uma região. 
Foram coletados os dados de idade, sexo (M/F) e salário. 
Faça um algoritmo que informe:
    a) a média de salário do grupo;
    b) maior e menor idade do grupo;
    c) quantidade de mulheres com salário até R$100,00.
Encerre a entrada de dados quando for digitada uma idade negativa. 
(Use o comando WHILE e não use vetores ou matrizes)
 """
contador  = maior_idade = mulher_salario= soma_salario = 0
menor_idade = 999999999
while True:
    idade = int(input('idade: '))
    if idade > 0:
        sexo = str(input('sexo[m,f]: '))
        salario = float(input('salario: '))
        contador +=1
        soma_salario = soma_salario + salario
        media_salario = soma_salario / contador
        if idade < menor_idade:
            menor_idade = idade
        if idade > maior_idade:
            maior_idade = idade
        if sexo == 'f' and salario > 0 and salario <= 100:
            mulher_salario += 1
    else:
        print(f'a media salarial do grupo é de {media_salario}')
        print(f'a menor idade do grupo é {menor_idade} e a maior é {maior_idade}')
        print(f'o numero de mulheres que recebe salário até R$100,00 é {mulher_salario}')
        break