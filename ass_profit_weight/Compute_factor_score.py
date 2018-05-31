import pandas as pd
import graduation.Factor_name
import graduation.Create_final_factor_data
import graduation.Calculate_profit
import graduation.Ticker

profit_weight = [0.110373182,
0.047201139,
0.162397217,
0.146505376,
0.152118912,
0.059930424,
0.139547755,
0.052024035,
0.129901961
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
        data.to_csv('F:/毕业设计/收益率赋权/'+str(factor_name) + '.csv')
    else:
        factor_name = graduation.Create_final_factor_data.name_list[i]
        df = graduation.Create_final_factor_data.d[factor_name].df
        order = graduation.Create_final_factor_data.d[factor_name].order
        data = pd.DataFrame(index=graduation.Ticker.List,columns=[x for x in range(732)])
        for k in range(732):
            for j in range(295):
                data.at[graduation.Ticker.List[order[k][j]],k] = abs(j-295)
        data = data*profit_weight[i]
        data.to_csv('F:/毕业设计/收益率赋权/'+str(factor_name) + '.csv')
