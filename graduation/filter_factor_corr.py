import pandas as pd
import graduation.Tradedate

file = open('F:/毕业设计/factor_filter.csv', 'r', newline='')
factor_filter_df = pd.read_csv(file,header=None)
file.close()
factor_filter_list = factor_filter_df.iloc[0]
df = pd.DataFrame()
for day in graduation.Tradedate.Date[0:1]:
    print(day)
    d = pd.DataFrame()
    data = pd.DataFrame()
    file = open('F:/毕业设计/std_factor_data/'+str(day) + '.csv', 'r', newline='')
    d = pd.read_csv(file)
    for i in range(len(factor_filter_list)):
        data[i] = d.iloc[int(factor_filter_list[i])]
    df = data.corr()
for day in graduation.Tradedate.Date[1:]:
    print(day)
    d = pd.DataFrame()
    data = pd.DataFrame()
    file = open('F:/毕业设计/std_factor_data/'+str(day) + '.csv', 'r', newline='')
    d = pd.read_csv(file)
    for i in range(len(factor_filter_list)):
        data[i] = d.iloc[int(factor_filter_list[i])]
    df += data.corr()
(df/732).to_csv('F:/毕业设计/filter_factor_corr.csv')
