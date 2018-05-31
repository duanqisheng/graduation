import pandas as pd
import numpy as np
import graduation.My_function
import csv
import graduation.Factor_name
import graduation.Tradedate


factor_IC_list = list()
file = open('F:/毕业设计/Section_in_time_profit.csv','r')
df_profit = pd.read_csv(file, index_col=0)
# print(df_profit.head(5))
file.close()
for factor_name in graduation.Factor_name.List:
    print(factor_name)
    profit_list = list()
    corr_list = list()
    factor_list = list()
    file = open('F:/毕业设计/Section_in_factor/'+str(factor_name)+'.csv','r')
    df = pd.read_csv(file, header=None)
    file.close()
    for i in range(df_profit.shape[1]-1):
        profit_list = df_profit[graduation.Tradedate.Date[i+1]]
        factor_list = df[i]
        corr_list.append(graduation.My_function.correlation_coefficent(profit_list, factor_list))
    corr_list= np.asarray(corr_list)
    factor_IC_list.append(corr_list.mean()*100)
file = open('F:/毕业设计/factor_IC.csv','w')
writer = csv.writer(file)
writer.writerow(factor_IC_list)
