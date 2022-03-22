""" Considere que o aumento dos funcionários de uma empresa é de 8% do salário atual mais um percentual de 
produtividade discutido com a empresa. Escrever um algoritmo que lê o número do funcionário, seu salário 
atual e o índice de produtividade discutido com a empresa. Então, escreve o número do funcionário, seu 
aumento e o valor de seu novo salário.  """

num_funcionario= int(input('qual o numero do funcionario: '))
salario_atual= float(input('qual o salario do funcionario: '))
perc_aumento= salario_atual * 0.08
perc_produtividade= salario_atual * (float(input('qual o percentual de produtividade: '))/100)

salario_novo= salario_atual + perc_aumento + perc_produtividade

print('o novo salario do funcionario '+ str(num_funcionario) + ' é de: R$ ' + str(salario_novo))
