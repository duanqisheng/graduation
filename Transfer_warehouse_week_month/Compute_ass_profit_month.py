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
file = open('F:/毕业设计/Transfer_warehouse_week_month/'+str(factor_name) + '.csv')
data = pd.read_csv(file,index_col=0)
file.close()
for i in range(1,9):
    factor_name = name_list[i]
    print(factor_name)
    file = open('F:/毕业设计/Transfer_warehouse_week_month/'+str(factor_name) + '.csv')
    df = pd.read_csv(file,index_col=0)
    data = data + df


for i in range(24):
    for j in range(30):
        data[str(i)] = data[str(i)]+data[str(j+1)]
profit_list = []
impack = -0.1
for j in range(23):
    print(j)
    if j == 0:
        group = pd.Series(data.sort_values(by=[str(j)])[str(j)][59*4:59*5]).index.tolist()
        for k in range(30):
            day = j*30+k+30
            # 计算等权高配组合
            profit_list.append(graduation.Calculate_profit.group_profit_for_dayi(group,day))
        oldlist = group
    else:
        group = pd.Series(data.sort_values(by=[str(j)])[str(j)][59*4:59*5]).index.tolist()
        for k in range(30):
            if k == 0:
                day = j*30+k+30
                profit_list.append(graduation.Calculate_profit.group_profit_for_dayi_impack(group,day,oldlist,impack))
            else:
                day = j*30+k+30
                profit_list.append(graduation.Calculate_profit.group_profit_for_dayi(group,day))
        oldlist = group
df = pd.DataFrame(profit_list)
df.to_csv('F:/毕业设计/Transfer_warehouse_week_month/ass_profit__month_01.csv')
file.close()
