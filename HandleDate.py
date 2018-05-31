
#这一段用来分割成各个因子在日期截面上的独立的csv文件
#文件大小是487*248的矩阵
import pandas as pd
import csv
import TradeDate
file2 = open('C:/Users/Administrator/Desktop/毕业设计/test.csv', 'r')
df = pd.read_csv(file2)

for DATE in TradeDate.List:
    newdate = ''
    for ele in DATE:
        if ele.isdigit():
            newdate += ele
        else:
            newdate += '_'
    with open('C:/Users/Administrator/Desktop/毕业设计/Date/'+str(newdate)+ '.csv', 'w' , newline='') as f:
        writer = csv.writer(f)
        for index, row in df.iterrows():
            if row[3] == DATE:
                data = row[2:]
                writer.writerow(data)
