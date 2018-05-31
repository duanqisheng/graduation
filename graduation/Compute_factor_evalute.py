import pandas as pd
import graduation.Factor_name
import graduation.My_function

data = []
market_profit_list = list()
file = open('F:/毕业设计/market_ass_profit.csv')
market_df = pd.read_csv(file,header=None)
file.close()
market_profit_list = market_df.iloc[0].tolist()
file = open('F:/毕业设计/factor_ass_profit.csv')
df = pd.read_csv(file, index_col=0)
file.close()
file = open('F:/毕业设计/factor_IC.csv')
IC_df = pd.read_csv(file, header=None)
file.close()
IC_list = IC_df.iloc[0].tolist()
for i in range(len(graduation.Factor_name.List)):
    list = []
    list.append(graduation.Factor_name.List[i])
    list.append(round(graduation.My_function.compute_accumulated_profit(df.iloc[i].tolist()),2))
    list.append(round(graduation.My_function.compute_annual_profit(df.iloc[i].tolist()),2))
    list.append(round(graduation.My_function.excess_profit(df.iloc[i].tolist(),market_profit_list),2))
    list.append(round(graduation.My_function.compute_probability_win(df.iloc[i].tolist(),market_profit_list),2))
    list.append(round(graduation.My_function.compute_IR(df.iloc[i].tolist()),2))
    list.append(round(IC_list[i],2))
    data.append(list)
data = pd.DataFrame(data)
data.to_csv('F:/毕业设计/factor_evalute.csv')
