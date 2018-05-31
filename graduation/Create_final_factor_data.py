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
        if self.name == 'ARBR':
            print('-------------------------------------')
            print('Load_finish!')
            print('-------------------------------------')
        self.order = list()
        for i in range(732):
            d_index = self.df.sort_values(by=i).index.tolist() # 升序排列
            self.order.append(d_index)


file = open('F:/毕业设计/factor_filter.csv')
d = pd.read_csv(file, header=None)
final_list = d.iloc[2][0:9]
file.close()
name_list = []
for factor in final_list:
    name_list.append(graduation.Factor_name.List[int(factor)])
d = {}
for name in name_list:
    d[str(name)] = DataFame(name)
