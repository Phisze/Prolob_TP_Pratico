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
else:
    print('A entrada deve seguir o seguinte padrão [".py .csv .pl"]')