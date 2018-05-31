import pandas as pd
import graduation.Factor_name
import graduation.Create_final_factor_data
import graduation.Calculate_profit


file = open('F:/毕业设计/factor_filter.csv')
d = pd.read_csv(file, header=None)
final_list = d.iloc[2][0:9]
file.close()
name_list = []
for factor in final_list:
    name_list.append(graduation.Factor_name.List[int(factor)])

for i in range(9):
    factor_name = graduation.Create_final_factor_data.name_list[i]
    print('factor_name')
    print(factor_name)
    df = graduation.Create_final_factor_data.d[factor_name].df
    order = graduation.Create_final_factor_data.d[factor_name].order
    data = []
    for k in range(5):
        print('group' + str(k))
        group = []
        group_profit = []
        for j in range(732):
            group = order[j][59*k:59*(k+1)]
            group_profit = graduation.Calculate_profit.group_profit(group)
        data.append(group_profit)
        print(data)
    data = pd.DataFrame(data)
    data.to_csv('F:/毕业设计/final_factor_group/'+str(factor_name) + '.csv')

