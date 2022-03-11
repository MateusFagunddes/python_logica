""" Escreva um algoritmo para ler o número de eleitores de um município, o número de votos brancos, nulos e válidos. 
Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.  """

num_eleitores= int(input('informe o numero de eleitores: '))
votos_brancos= int(input('informe o numero de votos brancos: '))
votos_nulos  = int(input('informe o numero de votos nulos: '))

porc_votos_brancos= votos_brancos/num_eleitores*100
porc_votos_nulos= votos_nulos/num_eleitores*100
porc_votos_validos= (num_eleitores-(votos_brancos + votos_nulos))/num_eleitores*100

print('A porcentagem de votos brancos é ' +
f'{porc_votos_brancos:.2f}'+ '%' + ', e a porcentagem de votos nulos é de '+ 
f'{porc_votos_nulos:.2f}' + '%, e a porcentagem de votos validos é de ' + f'{porc_votos_validos:.2f}'+'%')

