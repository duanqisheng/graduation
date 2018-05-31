import pandas as pd
import graduation.Factor_name
import graduation.Calculate_profit
import graduation.Ticker


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


profit_list = []
for j in range(731):
    print(j)
    group = pd.Series(data.sort_values(by=[str(j)])[str(j)][59*0:59*1]).index.tolist()
    # 计算等权低配组合
    profit_list.append(graduation.Calculate_profit.group_profit_for_dayi(group,j))
df = pd.DataFrame(profit_list)
df.to_csv('F:/毕业设计/ass_profit_1.csv')
file.close()
