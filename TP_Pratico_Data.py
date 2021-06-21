from pyswip import Prolog
import pandas as pd
import re
import sys

class prologData:
    prolog = Prolog()

    def __init__(self, nameCsv, namePl):
        sort = pd.read_csv(nameCsv)
        cols = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6']
        nums = sort[cols]
        self.prolog.dynamic('game/6')
        for index, row in nums.iterrows():
            self.prolog.assertz("game(" + str(row['X1']) + "," + str(row['X2']) + "," + str(row['X3']) + "," +
                           str(row['X4']) + "," + str(row['X5']) + "," + str(row['X6']) + ")")
        self.prolog.assertz("game(" + str(nums['X1'][0]) + "," + str(nums['X2'][0]) + "," + str(nums['X3'][0]) + "," +
                       str(nums['X4'][0]) + "," + str(nums['X5'][0]) + "," + str(nums['X6'][0]) + ")")

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
            res['X'] = re.findall(r'\d+', res['X'])
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
    print(p.game_sort_Q())
else:
    print('A entrada deve seguir o seguinte padrão [".py .csv .pl"]')