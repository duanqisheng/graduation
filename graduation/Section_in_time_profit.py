import graduation.Ticker
import pandas as pd


j = 0
profit = list()
for ticker in graduation.Ticker.com_List:
    j += 1
    print('这是第'+str(j)+'支股票')
    file = open('F:/毕业设计/profit/'+str(ticker) + '.csv')
    df = pd.read_csv(file)
    profit.append(df.iloc[0])
df = pd.DataFrame(profit)
df.to_csv('F:/毕业设计/Section_in_time_profit.csv')
