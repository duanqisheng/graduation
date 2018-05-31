import graduation.Tradedate
import pandas as pd


class DataFame:
    def __init__(self, day):
        file = open('F:/毕业设计/std_factor_data/'+str(day) + '.csv', 'r', newline='')
        self.df = pd.read_csv(file)
        self.name = day
        if self.name == '12_29_2017':
            print('Load_finish!')



d = {}
for day in graduation.Tradedate.Date:
    d[str(day)] = DataFame(day)
# print(d['2_25_2015'].df)
