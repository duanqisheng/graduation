# 分割收盘价等基本交易信息
# 只用执行一次
# 一只股票在732天的交易信息 732*25 其中第2列是股票代码（非补全），第五列是日期，第是一列是收盘价，16列是复权因子。

import csv
import graduation.Ticker
for ticker in graduation.Ticker.com_List:
    print(ticker)
    with open('F:/毕业设计/trade_data/'+str(ticker) + '.csv', 'w', newline='') as f:
        file = open('F:/毕业设计/trade_original_data_2015_2017.csv', 'r', encoding='UTF-8')
        reader = csv.reader(file)
        writer = csv.writer(f)
        for index, row in enumerate(reader):
            if row[2] == ticker:
                data = row
                writer.writerow(data)
