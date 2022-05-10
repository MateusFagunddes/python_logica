""" 9.	Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1 : feminino   2 : masculino)
 de uma pessoa, construa um algoritmo que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas: 
(a)	para homens: 		(72.7 * h) - 58 
(b)	para mulheres:  	(62.1 * h) - 44.7 
 """

altura= float(input('digite sua altura: '))
sexo=int(input('insira seu sexo(1 para mulher, 2 para homem): '))

if sexo == 1:
    peso= (62.1 * altura) - 44.7
if sexo== 2:
    peso= (72.7 * altura) - 58   
print(f'seu peso ideal é: {peso:.2f}')
