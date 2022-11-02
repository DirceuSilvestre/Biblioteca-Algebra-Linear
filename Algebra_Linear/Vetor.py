from cmath import sqrt
from random import randint


# --------------------- #

'''Criar vetor'''
# nulo
# unitario
# aleatorio
# oposto

'''Imprimir vetor'''

'''Igualdade de vetores'''

'''Calculos com vetores'''
# subtração
# soma
# produto escalar
# multiplicação por escalar
# divisao por escalar
# modulo

# --------------------- #


class Vetor:

    # metodos

    # o unico parametro é a dimensão, R², R³ ou maior

    # se não passar nenhum parametro, retorna vetor de R²
    def criar_vetor_nulo(self, dimensao=2):
            vector = [0] * dimensao
            return vector

    def criar_vetor_unitario(self, dimensao=2):
            vector = [1] * dimensao
            return vector

    # se não passar parametro retorna vetor do R² preenchido de forma aleatoria, entre 0 a 9
    def criar_vetor_aleatorio(self, dimensao=2):
            vector = []
            for i in range(dimensao):
                vector.append(randint(0, 9))
            return vector

    # para o vetor oposto tem que passar como parametro o vetor que quer o oposto dele
    def criar_vetor_oposto(self, vector):
        vetor_oposto = []
        for i in range(len(vector)):
            vetor_oposto.append(-vector[i])
        return vetor_oposto

    # imprime os vetores como a gente escreve no caderno
    # aceita a passagem de vários vetores de vetores em casa posição, se booleano igual a True, ou de varios vetores se for False
    def imprimir_vetor(self, plural=False, *args):
        if (plural):
            for linha_de_linha in range(len(args)):
                for linha in range(len(args[linha_de_linha])):
                    print('(', end='')
                    for coluna in range(len(args[0][linha])):
                        if (coluna == (len(args[0][linha]) - 1)):
                            print(str(args[0][linha][coluna]) + ')', end='\n')
                        else:
                            print(str(args[0][linha][coluna]) + ',', end=' ')
        else:
            for linha in range(len(args)):
                print('(', end='')
                for coluna in range(len(args[linha])):
                    if (coluna == (len(args[linha]) - 1)):
                        print(str(args[linha][coluna]) + ')', end='\n')
                    else:
                        print(str(args[linha][coluna]) + ',', end=' ')

    # aceita a passagem de mais de um vetor porém só compara dois vetores
    def igualdade_de_vetores(self, *args):
        tamanho = 0
        if (len(args[0]) == len(args[1])):
            for item in range(len(args[0])):
                if args[0][item] == args[1][item]:
                    tamanho += 1
                else:
                    break
            if(tamanho == len(args[1])):
                print("Vetores iguais", end='\n')
            else:
                print("Os vetores não são iguais", end='\n')
        else:
            print("Vetores de dimensões diferentes, então não são iguais", end='\n')

    # subtração de vetores do mesmo tamanho, não aceita vetor de vetores
    def subtracao_de_vetor(self, *args):
        for i in range(len(args) - 1):
            if (len(args[i]) != len(args[i + 1])):
                print("Não subtrai vetores de tamanhos diferentes", end='\n')
                return 0

        vetor_subtracao = []
        elemento = 0
        for linha in range(len(args)):
            for coluna in range(len(args[linha])):
                if ((coluna and elemento) == 0):
                    elemento = args[coluna][linha]
                else:
                    elemento -= args[coluna][linha]
            vetor_subtracao.append(elemento)
        return vetor_subtracao

    # soma de vetores do mesmo tamanho, não aceita vetor de vetores
    def soma_de_vetor(self, *args):
        for i in range(len(args) - 1):
            if (len(args[i]) != len(args[i + 1])):
                print("Não soma vetores de tamanhos diferentes", end='\n')
                return 0

        vetor_soma = []
        elemento = 0
        for linha in range(len(args)):
            for coluna in range(len(args[linha])):
                if ((coluna and elemento) == 0):
                    elemento = args[coluna][linha]
                else:
                    elemento += args[coluna][linha]
            vetor_soma.append(elemento)
        return vetor_soma

    # multiplica cada posição dos vetores e soma com a próxima, x*x + y*y + z*z...
    def produto_escalar_vetor(sef, *args):
        for i in range(len(args) - 1):
            if (len(args[i]) != len(args[i + 1])):
                print("Não calcula o produto escalar de vetores de tamanhos diferentes", end='\n')
                return 0

        produto_escalar = 0
        multiplicacao = 0
        for items in range(len(args[0])):
            for elementos in range(len(args)):
                if (elementos == 0):
                    multiplicacao = args[elementos][items]
                else:
                    multiplicacao *= args[elementos][items]
            produto_escalar += multiplicacao
        return produto_escalar

    # ao inves de retornar, altera os valores dos vetores passados por parâmetro
    def multiplicacao_por_escalar_vetor(self, *args, escalar):
        for items in range(len(args)):
            for elementos in range(len(args[items])):
                args[items][elementos] *= escalar

    # ao inves de retornar, altera os valores dos vetores passados por parâmetro
    def divisao_por_escalar_vetor(self, *args, escalar):
        for items in range(len(args)):
            for elementos in range(len(args[items])):
                args[items][elementos] /= escalar

    # retorna uma lista com o módulo de cada vetor que foi passado como parametro nos seus respectivos indices
    def modulo_vetor(self, *args):
        modulo = []
        quadrado = 0
        for items in range(len(args)):
            for elementos in range(len(args[items])):
                if (elementos == 0):
                    quadrado = args[items][elementos] ** 2
                else:
                    quadrado += args[items][elementos] ** 2
            modulo.append(sqrt(quadrado))
        return modulo

    '''def angulo_entre_vetor(self, vetor1, vetor2, print=False, returner=True):
        if (len(vetor1) == len(vetor2)):
            cima = Vetor.produto_escalar_vetor(vetor1, vetor2)
            baixo = Vetor.modulo_vetor(vetor1) * Vetor.modulo_vetor(vetor2)
            resultado = cima / baixo
            if (print):
                print(f'{math.degrees(math.acos(resultado))} graus')
            if (returner):
                return math.degrees(math.acos(resultado))

        else:
            print("Não há como calcular vetores de dimensões diferentes", end='\n')'''


# class Matriz:


# -----TESTES----- #

ve = Vetor()
vetor1 = ve.criar_vetor_unitario(4)
ve.imprimir_vetor(vetor1)
vetor2 = ve.criar_vetor_oposto(vetor1)
ve.imprimir_vetor(vetor2)
