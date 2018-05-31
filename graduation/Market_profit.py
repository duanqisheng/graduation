'''
# 用于计算市场组合的收益率，只用执行一次
import graduation.Calculate_profit
import csv

weight = []
for i in range(len(graduation.Tradedate.Date)):
    weight.append(1)
market_profit = graduation.Calculate_profit.ass_profit(weight)
with open('F:/毕业设计/market_ass_profit.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(market_profit)
'''
import csv
file = open('F:/毕业设计/market_ass_profit.csv','r',newline='')
reader = csv.reader(file)
profit = []
column =[row[2] for row in reader]
for index, rows in enumerate(reader):
    if index == 0:
        profit = rows

# print(profit)
netvalue = 1
for ele in profit:
    netvalue *= 1+float(ele)
print(netvalue)
print(column)
