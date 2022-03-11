""" 12.	Escreva um algoritmo para ler o número de gols marcados pelo Grêmio 
e o número de gols marcados pelo Inter em um GRENAL. Escreva o Nome do Vencedor. 
Caso não haja vencedor deverá ser impresso a palavra EMPATE. """

gol_gremio=int(input('insira o numero de gols marcados pelo Grêmio: '))
gol_Inter=int(input('insira o numero de gols marcados pelo Inter: '))

if gol_Inter> gol_gremio:
    print(f'Inter campeão! O jogo terminou em {gol_Inter}x{gol_gremio} para o Inter')
elif gol_gremio > gol_Inter:
    print(f'Grêmio campeão! O jogo terminou em {gol_gremio}x{gol_Inter} para o Grêmio')
elif gol_Inter == gol_gremio:
    print('Empate!')    