""" Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o 
código e o preço de custo de cada produto e calcule o preço novo. 
Calcule também, a média dos preços com e sem aumento. Mostre o código 
e o preço novo de cada produto e, no final, as médias. A entrada de dados 
deve terminar quando for lido um código de produto negativo. (Use o comando WHILE) """
media_precos_custo = 0
media_precos_att = 0
preco_custo_custo = 0
preco_novo_novo = 0
contador = 0
while True:
    cod_produto = int(input('codigo do produto: '))
    if cod_produto != 0:
        preco_custo = float(input('insira o prço de custo do produto: '))
        preco_novo = preco_custo +(preco_custo * 0.20)
        print('****'*20)
        print(f'o preço do produto {cod_produto}, atualizado em 20%, é de R${preco_novo:.2f}')
        print('****'*20)
        contador +=1
        preco_custo_custo += preco_custo
        preco_novo_novo += preco_novo
        media_precos_custo = preco_custo_custo/contador
        media_precos_att = preco_novo_novo/contador
    else:
        print(f'a media dos preços de custo é de {media_precos_custo}')
        print(f'a media dos preços atualizadso com 20% é de {media_precos_att}')
        break