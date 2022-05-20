""" 6. Procedimento para mostrar o resultado da eleição """
def eleicao():
    voto = -1
    candidato1 = candidato2 = candidato3 = candidato4 = votoNulo = votoBranco =0
    while voto != 0:
        print('para um voto válido, escolha uma das alternativas a baixo:')
        for i in range(4):
            print(f'digite{i+1} para o canditado {i+1}')
        print('digite 5 para voto nulo\n'+'digite 6 para voto em branco\n')
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


eleicao()