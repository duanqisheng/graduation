import pandas as pd
import csv

file = open('F:/毕业设计/factor_adjust_evalute.csv')
df = pd.read_csv(file,header=0)
file.close()
data = []
index_list = list()
List = list()
for i in range(243):
    if df['3'][i]>5 and df['5'][i]>10 and abs(df['6'][i])>1:
        List.append(df['0'][i])
        index_list.append(df['index'][i])
data.append(index_list)
data.append(List)
file = open('F:/毕业设计/factor_filter.csv','w',newline='')
writer = csv.writer(file)
writer.writerows(data)
