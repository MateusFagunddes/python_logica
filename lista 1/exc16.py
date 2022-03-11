""" A equipe McLaren deseja calcular o número mínimo de litros que deverá colocar no 
tanque de seu carro para que ele possa percorrer um determinado número de voltas 
até o primeiro reabastecimento. Escreva um algoritmo que leia o comprimento da pista (em metros), 
o número total de voltas a serem percorridas no grande prêmio, o número de reabastecimentos desejados, 
e o consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros 
necessários para percorrer até o primeiro reabastecimento. Obs: Considere que o número de voltas 
entre os reabastecimentos é o mesmo.  """

comprimento_pista= int(input('insira o comprimento da pista: ')) #7960 metros(interlagos)
num_total_voltas= int(input('insira o numeros de volta: ')) #24 voltas totais(numero de media de voltas na pista)
num_reabastecimento= int(input('insira o numeros de reabastecimentos desejados: ')) # 1 reabastecimento a cada 3 voltas (8 no total)
consumo_carro=  float(input('insira quanto litros são gastos por km: ')) #1.3km/l (media)

tota_pista_km = (comprimento_pista * num_total_voltas)/1000;
reabastecimento_km = tota_pista_km / (num_reabastecimento + 1)
minimo_litros = reabastecimento_km / consumo_carro

print('quantidade minima de litros necessarios para terminar a corrida é de ' +  f'{minimo_litros:.2f}'+'L')
