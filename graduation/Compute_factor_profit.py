import graduation.Create_factor_ass_data
import graduation.Factor_name
import pandas as pd

file = open('F:/毕业设计/Section_in_time_profit.csv')
df = pd.read_csv(file,index_col=0)
file.close()
result = list()
for factor in graduation.Factor_name.List:
    print(factor)
    factor_wight_df = graduation.Create_factor_ass_data.d[factor].df
    one_factor_profit = []
    for i in range(295):
        my_list = []
        for j in range(732):
            my_list.append(df.iloc[i,j] * factor_wight_df.iloc[j,i])
        one_factor_profit.append(my_list)
    one_factor_profit_df = pd.DataFrame(one_factor_profit)
    s = pd.Series(one_factor_profit_df.mean(axis=0)).tolist()
    result.append(s)
result = pd.DataFrame(result, index=graduation.Factor_name.List)
result.to_csv('F:/毕业设计/factor_ass_profit.csv')
