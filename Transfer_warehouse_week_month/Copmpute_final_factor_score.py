import pandas as pd
import graduation.Factor_name
import graduation.Create_final_factor_data
import graduation.Calculate_profit
import graduation.Ticker

for i in range(9):
    print('factor_name')
    if i == 8:
        factor_name = graduation.Create_final_factor_data.name_list[i]
        print(factor_name)
        df = graduation.Create_final_factor_data.d[factor_name].df
        order = graduation.Create_final_factor_data.d[factor_name].order
        data = pd.DataFrame(index=graduation.Ticker.List,columns=[x for x in range(732)])
        for k in range(732):
            for j in range(295):
                data.at[graduation.Ticker.List[order[k][j]],k] = j
        data.to_csv('F:/毕业设计/Transfer_warehouse_week_month/'+str(factor_name) + '.csv')
    else:
        factor_name = graduation.Create_final_factor_data.name_list[i]
        print(factor_name)
        df = graduation.Create_final_factor_data.d[factor_name].df
        order = graduation.Create_final_factor_data.d[factor_name].order
        data = pd.DataFrame(index=graduation.Ticker.List,columns=[x for x in range(732)])
        for k in range(732):
            for j in range(295):
                data.at[graduation.Ticker.List[order[k][j]],k] = abs(j-295)
        data.to_csv('F:/毕业设计/Transfer_warehouse_week_month/'+str(factor_name) + '.csv')
