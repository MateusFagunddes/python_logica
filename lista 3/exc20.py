""" Faça um algoritmo que leia vários números inteiros e 
calcule o somatório dos números negativos. O fim da 
leitura será indicado pelo número 0. """
soma = 0
while True:
    num = int(input('valor: '))
    if num != 0:
        if num < 0:
            soma += num
    else:
        print(f'a soma dos numeros negativos informados é de {soma}')
        break    
