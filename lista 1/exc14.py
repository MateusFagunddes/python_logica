""" Um motorista de taxi deseja calcular o rendimento de seu carro na praça. 
Sabendo-se que o preço do combustível é de R$ 4,50 , escreva um algoritmo para ler: 
a marcação do Hodômetro (Km) no início do dia, a marcação (Km) no final do dia, 
o número de litros de combustível gasto e o valor total (R$) recebido dos passageiros. 
Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia. """

preco_combustivel   = float(4.50)
hodometro_inicio_dia= float(input('quilometregem inicio do dia: '))
hodometro_fim_dia   = float(input('quilometregem final do dia: '))
combustivel_gasto   = float(input('combustivel gasto no dia: '))
recebidos           = float(input('quanto foi recebido no dia: '))

km_rodados= hodometro_fim_dia - hodometro_inicio_dia
media_consumo_combustivel= km_rodados / combustivel_gasto
gasto_com_combustivel= combustivel_gasto * preco_combustivel
lucro= recebidos - gasto_com_combustivel

print('media de consumo de combustivel: ' + f'{media_consumo_combustivel:.2f}')
print('quanto foi lucrado: '+ f'{lucro:.2f}')