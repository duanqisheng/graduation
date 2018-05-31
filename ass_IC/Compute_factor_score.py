import pandas as pd
import graduation.Factor_name
import graduation.Create_final_factor_data
import graduation.Calculate_profit
import graduation.Ticker

profit_weight = [0.101047904,
0.100299401,
0.142964072,
0.122754491,
0.137724551,
0.090568862,
0.112275449,
0.08008982,
0.112275449,
]

for i in range(9):
    print('factor_name')
    print(graduation.Create_final_factor_data.name_list[i])
    if i == 8:
        factor_name = graduation.Create_final_factor_data.name_list[i]
        df = graduation.Create_final_factor_data.d[factor_name].df
        order = graduation.Create_final_factor_data.d[factor_name].order
        data = pd.DataFrame(index=graduation.Ticker.List,columns=[x for x in range(732)])
        for k in range(732):
            for j in range(295):
                data.at[graduation.Ticker.List[order[k][j]],k] = j
        data = data*profit_weight[i]
        data.to_csv('F:/毕业设计/ass_IC/'+str(factor_name) + '.csv')
    else:
        factor_name = graduation.Create_final_factor_data.name_list[i]
        df = graduation.Create_final_factor_data.d[factor_name].df
        order = graduation.Create_final_factor_data.d[factor_name].order
        data = pd.DataFrame(index=graduation.Ticker.List,columns=[x for x in range(732)])
        for k in range(732):
            for j in range(295):
                data.at[graduation.Ticker.List[order[k][j]],k] = abs(j-295)
        data = data*profit_weight[i]
        data.to_csv('F:/毕业设计/ass_IC/'+str(factor_name) + '.csv')
