import Ticker
import csv
MarketProfitList = []
for day in range(243):
    profit = 0
    for ticker in Ticker.List:
        file = open('C:/Users/Administrator/Desktop/毕业设计/profit/'+str(ticker)+'.csv', 'r')
        reader = csv.reader(file)
        for i,rows in enumerate(reader):
            if i == 0:
                row = rows
            profit += float(row[day])
    profit /= 48
    MarketProfitList.append(profit)
print(MarketProfitList)
org = 1
for ele in MarketProfitList:
    org = org * (1+ele/100)
print(org)
