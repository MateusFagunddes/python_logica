""" 8.	Escreva um algoritmo que verifique a validade de uma senha fornecida pelo usuário. 
A senha válida é o número 1234. Deve ser impresso as seguintes mensagens: 
(a)	ACESSO PERMITIDO caso a senha seja válida
(b)	ACESSO NEGADO caso a senha seja inválida.
 """
senha_valida= 1234
senha=int(input('insira a senha: '))

if senha == senha_valida:
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO!')