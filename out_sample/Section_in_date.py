# 这一段用来分割成各个因子在日期截面上的独立的csv文件
# 文件大小是300*248的矩阵
# 只需要执行一次
import pandas as pd
import csv
import out_sample.tradedate
file = open('F:/毕业设计/样本外数据/final_factor.csv')
df = pd.read_csv(file)

for i in range(len(out_sample.tradedate.list)):
    print(out_sample.tradedate.list[i])
    print('!')
    with open('F:/毕业设计/样本外数据/Section_in_date/第'+str(i)+ '天.csv', 'w' , newline='') as f:
        writer = csv.writer(f)
        for j in range(362487):
            if df['tradeDate'][j] == out_sample.tradedate.list[i]:
                data = df.iloc[j]
                writer.writerow(data)
