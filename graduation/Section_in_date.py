# 这一段用来分割成各个因子在日期截面上的独立的csv文件
# 文件大小是300*248的矩阵
# 只需要执行一次
import pandas as pd
import csv
import graduation.Tradedate
file = open('F:/毕业设计/merge_original_data_2015_2017.csv', 'r')
df = pd.read_csv(file)

for day in graduation.Tradedate.Date:
    newdate = ''
    for ele in day:
        if ele.isdigit():
            newdate += ele
        else:
            newdate += '/'
    with open('F:/毕业设计/Section_in_date/'+str(day)+ '.csv', 'w' , newline='') as f:
        writer = csv.writer(f)
        for index, row in df.iterrows():
            if row[3] == newdate:
                data = row[2:]
                writer.writerow(data)
