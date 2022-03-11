""" Escreva um algoritmo para ler o salário mensal e o percentual de reajuste.
 Calcular e escrever o valor do novo salário.  """

salario_mensal= float(input('insira o salario mensal: '))
perc_reajuste= float(input('insira o reajuste: '))

calc_reajuste= salario_mensal + (salario_mensal* (perc_reajuste/100))

salario_novo= calc_reajuste

print('o salario novo é de: ' + str(salario_novo))