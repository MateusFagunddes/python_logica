""" A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:   

      a) média do salário da população; 
      b) média do número de filhos; 
      c) maior salário; 
      d) percentual de pessoas com salário até R$100,00. 

O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando WHILE)    """

contador = 1
totSalario=totalFilhos = media_salario = mediaFilhos =contador_menos_de_cem= salario_menos_de_cem= 0
while True:
    salario = float(input('Salario: '))
    if salario > 0:
        numFilhos = int(input('Filhos: '))
        totSalario += salario
        totalFilhos += numFilhos
        if salario <= 100:
            contador_menos_de_cem +=1
    else:
        break
    maior_salario = 0

    if salario > maior_salario:
        maior_salario = salario

    contador += 1

media_salario = totSalario / (contador - 1)
mediaFilhos = totalFilhos /(contador - 1) 

salario_menos_de_cem = contador_menos_de_cem*100 / (contador - 1)
    
print(f'A media salarial da população é de:R${media_salario}.' )
print(f'A media de filhos da população é de:{mediaFilhos}.' )
print(f'maior salario foi de : R${maior_salario}')
print(f'percentual de pessoas com salario menor que R$100,00 é de {salario_menos_de_cem}')
print(f'um total de {contador-1} habitantes foram ouvidos')