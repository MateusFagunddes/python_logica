"""Foi realizada uma pesquisa de algumas características físicas da 
população de uma certa região, a qual coletou os seguintes dados referentes 
a cada habitante para serem analisados:  
      - sexo (masculino e feminino)
      - cor dos olhos (azuis, verdes ou castanhos)
      - cor dos cabelos (louros, castanhos, pretos ou ruivos)
      - idade  
Faça um algoritmo que determine e escreva:   
      - a quantidade de homens com olhos azuis e idade maior que 20 anos
      - a quantidade de mulheres cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido por uma idade negativa."""
contador_homens = contador_mulheres = 0
while True:
    print('****' * 20)
    idade = int(input('idade: '))
    if idade > 0:
        sexo = str(input('sexo[m, f]: '))
        print('Insira a cor dos olhos:')
        print('1.azul')
        print('2.verdes')
        print('3.castanhos')
        cor_olhos = int(input('> '))
        print('Insira a cor dos cabelos:')
        print('1.louros')
        print('2.castanhos')
        print('3.pretos')
        print('4.ruivos')
        cor_cabelo = int(input('> '))
        if sexo == 'm' and cor_olhos == 1 and idade > 20:
            contador_homens += 1
        if sexo == 'f' and cor_olhos == 2 and cor_cabelo == 1 and idade >=18 and idade <=35:
            contador_mulheres += 1 
    else:
        print(f'a quantidade de homens com olhos azuis maiores de 20 anos é de {contador_homens}')
        print(f'a quantidade de mulhers com idade entre 18 e 35 anos loiras de olhos verdes é de {contador_mulheres}')
        break