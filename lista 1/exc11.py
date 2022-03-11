""" Escreva um algoritmo para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), 
calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes 
(considere que não será descontado a área ocupada por portas e janelas). Cada caixa de azulejos possui 2m2. """

comprimento= int(input('insira o comprimento: '))
largura = int(input('insira o largura: '))
altura = int(input('insira o altura: '))

Area_paredes = (2 * (comprimento*altura)) + (2*(largura * altura))
azulejos= Area_paredes/2
print('serão nescessarios '+ str(azulejos) + ' para cobrir todas as paredes')
