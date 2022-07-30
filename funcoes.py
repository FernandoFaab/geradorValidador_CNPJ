import random
from time import sleep
from lista import cnpj_list


def cnpj_input(*args, **kwargs):
    """
    Aqui ele irá pedir que o usuário digite um CNPJ. Depois a função eliminara os caracteres, usando a função
    remover_caracteres. Depois ele pegará o resultado, e verificará se contem apenas números. Se sim, ele retorna
    o input. Caso tenha letras, ele retornará erro e pedirá que digite novamente.
    :param args: recebe um input do CNPJ.
    :param kwargs: Remove os caracteres do CNPJ.
    :return: Retorna o CNPJ ou Erro, se tiver letras no meio do CNPJ.
    """
    while True:
        valor = str(input('Digite um CNPJ: '))
        cnpj_limpo = remover_caracteres(valor)
        try:
            int(cnpj_limpo)
            return cnpj_limpo
        except ValueError:
            print("\033[31mERRO! O número de CNPJ, não contem letras.\033[m")
            continue


def remover_caracteres(valor):
    """
    Removedor de caracteres do cnpj
    :param valor: recebe o cnpj com caracteres
    :return: retorna o cnpj sem caracteres
    """
    caracteres = './-'
    cnpj = ''.join(x for x in valor if x not in caracteres)
    return cnpj


def no_digit(x):
    """
    Esta função remove os digitos verificadores do CNPJ
    :param x: Recebe o CNPJ
    :return: Retorna o CNPJ sem os digitos verificadores
    """
    valor = (list(map(int, x[:-2])))
    return valor


def formula(x):
    """
    Calcula os dígitos verificadores, através do resultado da soma das fórmulas.
    :param x: recebe o produto da multiplicação dos números do CNPJ.
    :return: Realizar a soma dos produtos da multiplicação, ele aplica a fórmula de verificação e retorna o resultado.
    """
    soma = (11 - (sum(x) % 11))
    if soma <= 9:
        return soma
    else:
        return 0


def sequencia(valor):
    """
    Verifica se o CNPJ informado é uma sequência de números repetidos.
    :param valor: Receve o CNPJ informado.
    :return: Retorna se é ou não sequência.
    """
    x = valor
    if len(set(x)) == 1:
        return False
    else:
        return True


def validador(cnpj):
    """
    Esta é a função que valida o CNPJ. Primeiro ela verifica se é uma sequência numérica, caso não for ela compara
    o valor inserido pelo usuário, com o valor gerado pelas fórmulas.
    :param cnpj: Recebe o valor gerado após os calculos do programa.
    :return: retorna o False ou True para o usuário.
    """
    if sequencia(cnpj_list) == False:
        print('\033[31mCNPJ INVÁLIDO! É uma sequência\033[m')
    else:
        if cnpj != cnpj_list:
            print('\033[31mCNPJ INVÁLIDO!\033[m')
        else:
            print('\033[34mCNPJ VÁLIDO\033[m')


def gerador():
    """
    Gera randomicamente, um CNPJ sem os digitos verificadores.
    :return: CNPJ sem digitos verificadores.
    """
    inicio = []
    final = [0, 0, 0, 1]
    for x in range(0, 8):
        y = random.randint(0, 9)
        inicio.append(y)
    inicio.extend(final)

    return inicio


def caracteres(valor):
    """
    Receve os cnpj criado pelas fórmulas, e devolve com os caracteres.
    :param valor: CNJP
    :return: CNPJ com caracteres
    """
    cnpj = valor
    cnpj.insert(2, '.')
    cnpj.insert(6, '.')
    cnpj.insert(10, '/')
    cnpj.insert(15, '-')
    return cnpj


def finalizar():
    print('\033[31mFINALIZANDO\033[m', end='')
    sleep(0.5)
    print('\033[31m.\033[m', end='')
    sleep(0.5)
    print('\033[31m.\033[m', end='')
    sleep(0.5)
    print('\033[31m.\033[m', end='')
    sleep(0.5)
    print()







