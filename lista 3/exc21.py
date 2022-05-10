""" Faça um algoritmo que leia vários números inteiros e positivos e
calcule o produto dos números pares. O fim da leitura será indicado 
pelo número 0. """
produto = 1
while True:
    num = int(input('valor: '))
    if num > 0:
        if num % 2 ==0:
            produto *= num
    if num == 0:
        print(f'o produto dos numeros pares informados é {produto}')
        break
    if num < 0:
        print('insira um valor positivo!')