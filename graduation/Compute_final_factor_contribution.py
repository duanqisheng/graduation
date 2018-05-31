import pandas as pd
import graduation.Factor_name
import graduation.Calculate_profit
import graduation.Ticker
import numpy as np


file = open('F:/毕业设计/factor_filter.csv')
d = pd.read_csv(file, header=None)
final_list = d.iloc[2][0:9]
file.close()
name_list = []
for factor in final_list:
    name_list.append(graduation.Factor_name.List[int(factor)])

factor_name = name_list[0]
file = open('F:/毕业设计/effective_factor_weight_score/'+str(factor_name) + '.csv')
data = pd.read_csv(file,index_col=0)
file.close()
for i in range(1,9):
    factor_name = name_list[i]
    print(factor_name)
    file = open('F:/毕业设计/effective_factor_weight_score/'+str(factor_name) + '.csv')
    df = pd.read_csv(file,index_col=0)
    data = data + df


# 计算总分数
contricution_df = pd.DataFrame()
con = []
# 计算贡献度
for i in range(9):
    list = []
    factor_name = name_list[i]
    print(factor_name)
    file = open('F:/毕业设计/effective_factor_weight_score/'+str(factor_name) + '.csv')
    df = pd.read_csv(file,index_col=0)
    for k in range(1,732):
        one_dat_con = []
        sorted_data =data.sort_values(by=str(k))[str(k)][59*4:59*5]
        contricution_df[str(k)] = df[str(k)]/sorted_data
        for ele in contricution_df[str(k)].fillna('miss'):
            if ele != 'miss':
                one_dat_con.append(ele)
        list.append(pd.Series(one_dat_con).mean())
    con.append(list)
pd.DataFrame(con).to_csv('F:/毕业设计/6666.csv')
