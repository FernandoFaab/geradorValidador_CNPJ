""" Gerador e Validador de CNPJ """
from funcoes import finalizar, caracteres, gerador, validador, formula, no_digit, cnpj_input
from lista import cnpj_list, cnpj_notDigit, multiplicador

while True:
    resposta = int(input('\033[32mDeseja gerar[1], validar[2] e finalizar[3]? \033[m'))
    cnpj_list.clear()
    cnpj_notDigit.clear()
    if resposta == 2:
        valor = cnpj_input()
        cnpj_list.extend(list(map(int, valor)))
        cnpj_notDigit.extend(no_digit(cnpj_list))
        produto1 = list(map(lambda x, y: x * y, cnpj_notDigit, multiplicador[1:]))
        soma1 = formula(produto1)
        cnpj_notDigit.append(soma1)
        produto2 = list(map(lambda x, y: x * y, cnpj_notDigit, multiplicador))
        soma2 = formula(produto2)
        cnpj_notDigit.append(soma2)
        validador(cnpj_notDigit)
    if resposta == 1:
        cnpj = gerador()
        produto3 = list(map(lambda x, y: x * y, cnpj, multiplicador[1:]))
        soma3 = formula(produto3)
        cnpj.append(soma3)
        produto4 = list(map(lambda x, y: x * y, cnpj, multiplicador))
        soma4 = formula(produto4)
        cnpj.append(soma4)
        cnpj_caracteres = caracteres(cnpj)
        for x in cnpj_caracteres:
            print(x, end='')
        print()
    if resposta == 3:
        finalizar()
        break







