import pandas as pd
import csv
import graduation.Create_factor_std_Dataframe
# 分割因子数据

List = ['DAVOL20','ARBR','DEA','LFLO','Hurst','MA10RegressCoeff12','MoneyFlow20','PVT','TVSTD20']
for i in range(len(List)):
    data = []
    j = 0
    for ticker in graduation.Ticker.com_List:
        j += 1
        print('这是第'+str(j)+'支股票')
        profit = pd.Series
        factor = list()
        file = open('F:/毕业设计/profit/'+str(ticker) + '.csv')
        df = pd.read_csv(file)
        profit = df.iloc[0][1:] # 这个profit好像后面没用到
        file.close()
        for day in graduation.Tradedate.Date:
            df = graduation.Create_factor_std_Dataframe.d[str(day)].df
            if df[graduation.Ticker.List[j-1]][i]:
                factor.append(df[graduation.Ticker.List[j-1]][i])
            else:
                factor.append(0)
        data.append(factor)
    file = open('F:/毕业设计/Section_in_factor/'+str(graduation.Factor_name.List[i]) + '.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerows(data)
