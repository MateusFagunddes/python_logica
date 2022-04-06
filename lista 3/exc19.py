""" Faça um algoritmo que leia uma quantidade não determinada de números positivos. 
Calcule a quantidade de números pares e ímpares, a média de valores pares e a 
média geral dos números lidos. O número que encerrará a leitura será zero.  """

contador_par= contador_impar= total_num =0
while True:
    num = int(input('numero: '))
    if num ==0 or num < 0:
        break
    if num > 0:
        total_num +=1
        if num % 2 == 0:
            contador_par+=1

        
        if num % 2 != 0:
            contador_impar+=1
valores_pares = (contador_par/total_num)*100
print(f'a quantidade de numeros pares é de {contador_par}')
print(f'a quantidade de numeros impares é de {contador_impar}')
print(f'A quantidade de numeros informados foi {total_num} numeros e porcentagem de numeros pares foi de {valores_pares}%')

