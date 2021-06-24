from pyswip import Prolog
import pandas as pd
import re
import sys


class prologData:
    prolog = Prolog()

    def __init__(self, nameCsv, namePl):
        sort = pd.read_csv(nameCsv, header=None)
        sort = sort.iloc[1:]
        cols = [2, 3, 4, 5, 6, 7, 8]
        nums = sort[cols]
        self.prolog.dynamic('game/2')
        for index, row in nums.iterrows():
            self.prolog.assertz("game([" + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "," +
                           str(row[5]) + "," + str(row[6]) + "," + str(row[7]) + "]," + str(row[8]) + ")")
        self.prolog.assertz("game([" + str(nums[2][1]) + "," + str(nums[3][1]) + "," + str(nums[4][1]) + "," +
                          str(nums[5][1]) + "," + str(nums[6][1]) + "," + str(nums[7][1]) + "]," + str(nums[8][1]) + ")")
        self.prolog.consult(namePl)

    def has_number_sorted(self, A: int):
        t = list()
        for res in self.prolog.query("has_number_sorted(" + str(A) + ")."):
            t.append(res)
        return t
    
    def has_jogo_contemplado(self, X1: int, X2: int, X3: int, X4: int, X5: int, X6: int):
        t = list()
        for res in self.prolog.query("has_jogo_contemplado(" + str(X1) + "," + str(X2) + "," + str(X3) + "," + str(X4) + "," + str(X5) + "," + str(X6) + ")."):
            t.append(res)
        return t

    def game_sort_Q(self):
        t = list()
        for res in self.prolog.query("game_sort_Q(N, X)."):
            t.append(res)
        return t

    def qtde_X(self, num):
        t = list()
        for res in self.prolog.query("qtde_X("+str(num)+", N)."):
            t.append(res)
        return t

    def never_sort(self):
        t = list()
        for res in self.prolog.query("never_sort(X)."):
            t.append(res)
        return t

    def game_sort_N(self):
        t = list()
        for res in self.prolog.query("game_sort_N(X, N)."):
            t.append(res)
        return t


if len(sys.argv) == 3:
    csv = ''
    pl = ''
    if sys.argv[1][-4:] == '.csv':
        csv = sys.argv[1]
    else:
        print('O primeiro paramentro precisa ser um CSV')
        exit(1)
    if sys.argv[2][-3:] == '.pl':
        pl = sys.argv[2]
    else:
        print('O segundo paramentro precisa ser um prolog')
        exit(1)

    p = prologData(csv, pl)
    print(p.game_sort_N())
    print(p.has_number_sorted(72))

    num = 0
    mensagem = """### -- SISTEMA PROLOG DE CONSULTA DE MEGA SENA -- ###"
    "-- Digite uma das opções abaixo para consultar a base de dados da Mega Sena."
        Digite um número igual ou abaixo de 0 para encerrar o programa --
        -> 1 - Verificar se um número X foi sorteado
        -> 2 - Verificar qual número nunca foi sorteado
        -> 3 - Verificar se um jogo(X1,X2,X3,X4,X5,X6) já foi contemplado
        -> 4 - Verificar se algum jogo completo já foi contemplado mais de uma vez
        -> 5 - Verificar quantas vezes um número X foi sorteado
        -> 6 - Verificar qual número foi o mais sorteado"""

    while True:
        print(mensagem)
        num = int(input("* Digite a sua opção: "))
        if num <= 0:
            break

        # Opções de consulta

        # Verificar se um número X foi sorteado
        if num == 1:
            a = int(input("Digite um número para verificar se ele foi sorteado ou não: "))
            res_list = p.has_number_sorted(a)
            if len(res_list) == 0:
                print("Número não foi sorteado")
            else:
                print("O número digitado foi sorteado!")

        # 2 - Verificar qual número nunca foi sorteado TODO = corrigir essa parte
        elif num == 2:
            res_list = p.never_sort()
            if len(res_list) == 0:
                print("Todos os números já foram sorteados.")
            else:
                print("Os números: " + str(res_list[0]["X"]) + " nunca foram sorteados.")

        # Verificar se um jogo(X1,X2,X3,X4,X5,X6) já foi contemplado
        elif num == 3:
            x1 = int(input("Digite o primeiro número do jogo: "))
            x2 = int(input("Digite o segundo número do jogo: "))
            x3 = int(input("Digite o terceiro número do jogo: "))
            x4 = int(input("Digite o quarto número do jogo: "))
            x5 = int(input("Digite o quinto número do jogo: "))
            x6 = int(input("Digite o sexto número do jogo: "))

            res_list = p.has_jogo_contemplado(x1, x2, x3, x4, x5, x6)

            if len(res_list) == 0:
                print("O jogo nunca foi contemplado.")
            else:
                print("O jogo já foi contemplado!")

        # Verificar se algum jogo completo já foi contemplado mais de uma vez
        elif num == 4:
            res_list = p.game_sort_N()

            if len(res_list) == 0:
                print("Nenhum jogo foi contemplado mais de uma vez.")
            else:
                print("O jogo: " + str(res_list[0]["X"]) + " foi contemplado " + str(res_list[0]["N"]) + " vezes!")

        # Verificar se um número X foi sorteado mais de uma vez
        elif num == 5:
            a = int(input("Digite um número para verificar quantas vezes ele foi sorteado: "))
            res_list = p.qtde_X(a)

            if len(res_list) == 0 or res_list[0]["N"] == 0:
                print("Número nunca foi sorteado.")
            else:
                print("O número " + str(a) + " foi sorteado " + str(res_list[0]["N"]) + " vezes!")

        # Verificar qual número foi o mais sorteado
        elif num == 6:
            res_list = p.game_sort_Q()

            if len(res_list) == 0:
                print("Não foi possível achar o número mais sorteado.")
            else:
                print("O número " + str(res_list[0]["N"]) + " foi o mais sorteado com " + str(res_list[0]["X"]) +
                      " ocorrências")


else:
    print('A entrada deve seguir o seguinte padrão [".py .csv .pl"]')