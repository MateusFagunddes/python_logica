""" Em uma eleição presidencial existem quatro candidatos. 
Os votos são informados através de códigos. Os dados 
utilizados para a contagem dos votos obedecem à seguinte codificação:    
      - 1,2,3,4 = voto para os respectivos candidatos; 
      - 5 = voto nulo; 
      - 6 = voto em branco;
Elabore um algoritmo que leia o código do candidato em um voto. Calcule e escreva: 
      - total de votos para cada candidato; 
      - total de votos nulos; 
      - total de votos em branco; 
Como finalizador do conjunto de votos, tem-se o valor 0. 
 """
voto = -1
candidato1 = candidato2 = candidato3 = candidato4 = votoNulo = votoBranco =0
while voto != 0:
    print('para um voto válido, escolha uma das alternativas a baixo:')
    print('digite 1 para candidato 1')
    print('digite 2 para candidato 2')
    print('digite 3 para candidato 3')
    print('digite 4 para candidato 4')
    print('digite 5 para voto nulo')
    print('digite 6 para voto em branco')
    voto =  int(input('seu voto: '))      
    print('====' *12)
    if voto == -1 or voto == 1 or voto == 2 or voto == 3 or voto == 4 or voto == 5 or voto == 6:
        if voto == 1:
            candidato1 += 1 
        if voto == 2:
            candidato2 += 1 
        if voto == 3:
            candidato3 += 1 
        if voto == 4:
            candidato4 += 1 
        if voto == 5:
            votoNulo += 1 
        if voto == 6:
            votoBranco += 1 
print('-_=_' *12)
print(f'o total de votos para o candidato 1 foi de : {candidato1}')
print(f'o total de votos para o candidato 2 foi de : {candidato2}')
print(f'o total de votos para o candidato 3 foi de : {candidato3}')
print(f'o total de votos para o candidato 4 foi de : {candidato4}')
print(f'o total de votos nulos foi de : {votoNulo}')
print(f'o total de votos em branco foi de : {votoBranco}')
print('-_=_' *12)