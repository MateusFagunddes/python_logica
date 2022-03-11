""" Uma loja vende bicicletas com um acréscimo de 50% sobre o seu preço de custo. 
Ela paga a cada vendedor 2 salários mínimos mensais, mais uma comissão de 15% 
sobre o preço de custo de cada bicicleta vendida, dividida igualmente entre eles. 
Escreva um algoritmo que leia o número de empregados da loja, o valor do salário 
mínimo, o preço de custo de cada bicicleta, o número de bicicletas vendidas, calcule e escreva: 
O salário final de cada empregado e o lucro (líquido) da loja.  """

num_empregados= int(input('quantos empregados à na loja? '))
salario_minimo= float(input('salario minimo é de: '))
preco_custo_bicicleta= float(input('o preço de custo de cada bicicleta é de: '))
num_bicicletas_vendidas= int(input('a quantidade de bicicletas vendidas esse mês foi de: '))


preco_venda= preco_custo_bicicleta+(preco_custo_bicicleta*0.50)
comissao=((preco_custo_bicicleta * num_bicicletas_vendidas)*0.15)/num_empregados
total_vendido= preco_venda * num_bicicletas_vendidas

salario_empregado= (salario_minimo*2) + comissao
despesa= (preco_custo_bicicleta*num_bicicletas_vendidas)+ (salario_empregado*num_empregados)
lucro= total_vendido - despesa

print('cada empregado receberá o salario de:R$' f'{salario_empregado:.2f}'+
' e o lucro total da empresa será de: R$' f'{lucro:.2f}')





