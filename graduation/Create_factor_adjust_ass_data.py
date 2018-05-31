import graduation.Factor_name
import pandas as pd
import graduation.Ticker
import graduation.Tradedate


class DataFame:
    def __init__(self, factor_name):
        file = open('F:/毕业设计/Adjust_factor_ass_weight/'+str(factor_name) + '.csv', 'r', newline='')
        self.df = pd.read_csv(file, index_col=0, header=0)
        self.name = factor_name
        print(self.name)
        if self.name == 'JDQS20':
            print('--------------------------------------')
            print('Load_finish!')
            print('--------------------------------------')


d = {}
for name in graduation.Factor_name.List:
    d[str(name)] = DataFame(name)
# print(d['AccountsPayablesTDays'].df)


