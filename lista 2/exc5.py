""" 5.	Escreva um algoritmo para ler o ano de nascimento de uma pessoa 
e Escreva uma mensagem que diga Se ela poderá ou não votar este ano 
(não é necessário considerar o mês em que ela nasceu). """

ano_nascimento=int(input('insira o seu ano de nascimento: '))
idade= 2022 - ano_nascimento

if idade >= 18:
    print('você podera votar esse ano')
else:
    print('você não podera votar esse ano')