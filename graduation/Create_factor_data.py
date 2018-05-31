
import graduation.Factor_name
import pandas as pd
import graduation.Ticker
import graduation.Tradedate


class DataFame:
    def __init__(self, factor_name):
        file = open('F:/毕业设计/Section_in_factor/'+str(factor_name) + '.csv', 'r', newline='')
        self.df = pd.read_csv(file, index_col=False,header=None)
        self.name = factor_name
        print(self.name)
        if self.name == 'JDQS20':
            print('------------------------')
            print('Load_finish!')
        self.order = list()
        for i in range(732):
            d_index = self.df.sort_values(by=i).index.tolist()
            self.order.append(d_index)


d = {}
for name in graduation.Factor_name.List:
    d[str(name)] = DataFame(name)
# print(d['AD20'].df)

