""" Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, 
mais uma comissão fixa por cada carro vendido. Além disso, ela também adiciona ao salário de 
cada vendedor 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que lê o número
 do vendedor, o salário fixo, o número de carros por ele vendidos, o valor total de suas vendas 
 e a comissão fixo que recebe por carro vendido e, sem seguida, calcule o salário do vendedor 
 juntamente com o seu número de identificação.  """

num_funcionario= int(input('qual o numero do funcionario: '))
salario_fixo= float(input('qual o salario do funcionario: '))
num_carros_vendidos= int(input('numero de carros vendidos: '))
total_vendas= float(input('quanto foi vendido pelo funcionario: '))
comi_fixa= total_vendas * 0.05
comi_vendas= total_vendas * (num_carros_vendidos/100)
salario_mes= salario_fixo + comi_fixa + comi_vendas

print('o salario do mês do fincionario '+ str(num_funcionario)+' foi de: R$'+ str(salario_mes))
