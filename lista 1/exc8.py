""" Escreva um algoritmo para ler o salário atual e o percentual de reajuste.
 Calcular e escrever o valor do novo salário.  """

salario_atual= float(input('insira o salario atual: '))
perc_reajuste= float(input('insira o reajuste: '))

salario_novo= salario_atual + (salario_atual* (perc_reajuste/100))

print('o salario novo é de: ' + str(salario_novo))