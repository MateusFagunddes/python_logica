""" Um mercado está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg 
Morango: R$ 5,00 p/Kg 
Maçã: R$ 3,00 p/Kg
Acima de 5 Kg 
Morango: R$ 4,00 p/Kg 
Maçã:R$ 2,00 p/Kg 
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
ultrapassar R$ 35,00, receberá ainda um desconto de 20% sobre esse total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade 
(em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente. """
morangos_comprados= int(input('auntos quilos de morangos foram comprados: ')) 
macas_compradas= int(input('auntos quilos de morangos foram comprados: '))

peso_total= morangos_comprados + macas_compradas

if morangos_comprados <=5 and macas_compradas<=5:
    total= (5.00 * morangos_comprados) + (3.00 * macas_compradas)
    
if morangos_comprados >5 and macas_compradas>5:
    total= (4.00 * morangos_comprados) + (2.00 * macas_compradas)
    

if total >= 35.00 or peso_total >= 8:
    total = total - (total*0.20)
    

print(f'O total da compra deu {total}')