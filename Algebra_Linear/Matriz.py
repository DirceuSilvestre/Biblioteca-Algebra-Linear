from gettext import NullTranslations
import math
from operator import le
from random import randint
from math import sqrt

# Operações com Matrizes #

'''Criar Matriz'''
# nula
# unitaria
# random
# identidade

'''Imprimir'''
# imprime

'''Igualdade'''
# igualdade

'''Calculos com Matrizes'''
# soma
# subtração
# produto escalar
# multiplicação por escalar
# potencia
# traco
# determinante
# transposta
# simetrica


# ----------------------- #

def cria_matriz_aleatoria(linha, coluna):
    matriz = []
    for x in range(linha):
        partes = []
        for y in range(coluna):
            partes.append(randint(0, 9))
        matriz.append(partes)

    return matriz


def cria_matriz_nula(linha, coluna):
    matriz = []
    for x in range(linha):
        partes = []
        for y in range(coluna):
            partes.append(0)
        matriz.append(partes)

    return matriz


def cria_matriz_unitaria(linha, coluna):
    matriz = []
    for x in range(linha):
        partes = []
        for y in range(coluna):
            partes.append(1)
        matriz.append(partes)

    return matriz


def cria_matriz_identidade(tamanho):
    matriz = []
    for x in range(tamanho):
        partes = []
        for y in range(tamanho):
            if x == y:
                partes.append(1)
            else:
                partes.append(0)
        matriz.append(partes)

    return matriz


def imprime_matriz(vetor):
    for x in range(len(vetor)):
        print('|', end='')
        for y in range(len(vetor[0])):
            print(vetor[x][y], end=" ")
        print('|', end='')
        print()
    print()


def igualdade_matriz(matriz1, matriz2):
    tamanho = 0
    items = len(matriz1) * len(matriz1[0])
    if ((len(matriz1) == len(matriz2)) and (len(matriz1[0]) == len(matriz2[0]))):
        for l in range(len(matriz1)):
            for c in range(len(matriz1[0])):
                if (matriz1[l][c] == matriz2[l][c]):
                    tamanho += 1
                else:
                    break

        if(tamanho == items):
            print("Matrizes iguais", end='\n')
        else:
            print("As matrizes não são iguais", end='\n')
    else:
        print("Matrizes de dimensões diferentes", end='\n')


def soma_matriz(a, b):
    if (len(a) == len(b) and len(a[0]) == len(b[0])):
        tamanho_linha = len(a)
        tamanho_coluna = len(a[0])
        matriz = cria_matriz_nula(tamanho_linha, tamanho_coluna)
        for x in range(tamanho_linha):
            for y in range(tamanho_coluna):
                matriz[x][y] = a[x][y] + b[x][y]
        return matriz

    else:
        print("Não há como calcular matrizes de dimensões diferentes", end='\n')


def subtracao_matriz(a, b):
    if (len(a) == len(b) and len(a[0]) == len(b[0])):
        tamanho_linha = len(a)
        tamanho_coluna = len(a[0])
        matriz = cria_matriz_nula(tamanho_linha, tamanho_coluna)
        for x in range(tamanho_linha):
            for y in range(tamanho_coluna):
                matriz[x][y] = a[x][y] - b[x][y]
        return matriz

    else:
        print("Não há como calcular matrizes de dimensões diferentes", end='\n')


def multiplicacao_matriz_por_escalar(matriz, escalar):
    tamanho_linha = len(matriz)
    tamanho_coluna = len(matriz[0])
    for x in range(tamanho_linha):
        for y in range(tamanho_coluna):
            matriz[x][y] = matriz[x][y] * escalar
    return matriz


def produto_escalar_matriz(matriz1, matriz2):
    tamanho_coluna = len(matriz1[0])
    tamanho_linha = len(matriz2)
    if (tamanho_coluna == tamanho_linha):
        matriz3 = cria_matriz_nula(len(matriz1), len(matriz2[0]))
        for li in range(len(matriz1)):
            for c in range(len(matriz2[0])):
                for seg in range(tamanho_coluna):
                    matriz3[li][c] += matriz1[li][seg] * matriz2[seg][c]
        return matriz3

    else:
        print("Não é possível", end='\n')


def potencia_matriz(matriz, expoente):

    tamanho_linha = len(matriz)
    tamanho_coluna = len(matriz[0])
    
    resultado = matriz
    
    if (tamanho_linha != tamanho_coluna):
        print("Só há como calular matriz quadrada", end='\n')
    
    elif expoente == 0:
        return cria_matriz_identidade(tamanho_linha)

    elif (expoente == 1):
        return matriz

    elif (expoente >= 2):
        for i in range(1, expoente):
            resultado = produto_escalar_matriz(resultado, matriz)
        return resultado

    else:
        print("Não há como calcular matriz de expoente negativo")


def traco_matriz(matriz):
    traco = 0
    tamanho_linha = len(matriz)
    tamanho_coluna = len(matriz[0])
    for l in range(tamanho_linha):
        for c in range(tamanho_coluna):
            if l == c:
                traco += matriz[l][c]
    return traco


'''def determinante(matriz):
    final = len(matriz[0]) - 1
    diagonal_principal = 1
    diagonal_secundaria = 1
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if l == c:
                diagonal_principal *= matriz[l][c]
                diagonal_secundaria *= matriz[l][final]
                final -= 1
    return diagonal_principal - diagonal_secundaria'''


def transposta(matriz):
    linha = len(matriz[0])
    coluna = len(matriz)
    matriz_transposta = cria_matriz_nula(linha, coluna)
    for lin in range(linha):
        for col in range(coluna):
            matriz_transposta[lin][col] = matriz[col][lin]
    return matriz_transposta


def matriz_simetrica(matriz1, matriz2):
    saida = False
    for linha in range(len(matriz1)):
        for coluna in range(len(matriz1[0])):
            if(matriz1[linha][coluna] == matriz2[coluna][linha]):
                continue
            else:
                saida = True
                print("Não são simétricas", end="\n")
                break

        if (saida):
            break
    if(not saida):
        print("São simétricas", end="\n")
