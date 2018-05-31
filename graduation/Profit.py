# 1*732 的矩阵，记录每个交易日的涨跌值
import csv
import graduation.Ticker
import graduation.Tradedate
for ticker in graduation.Ticker.com_List:
    file = open('F:/毕业设计/trade_data/'+str(ticker)+'.csv', 'r')
    reader = csv.reader(file)
    profit = []
    for row in reader:
        if row:
            profit.append(float(row[19])*100)
    print(len(profit))
    with open('F:/毕业设计/profit/'+str(ticker) + '.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(graduation.Tradedate.Date)
        writer.writerow(profit)
