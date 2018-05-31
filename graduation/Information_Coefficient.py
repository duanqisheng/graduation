import graduation.Ticker
import graduation.Tradedate
import csv
import graduation.Factor_name
for i in range(1):#len(graduation.Factor_name.List)
    data = []
    j = 0
    for ticker in graduation.Ticker.com_List:
        j += 1
        print('这是第'+str(j)+'支股票')
        profit = []
        factor = []
        file = open('F:/毕业设计/profit/'+str(ticker) + '.csv', 'r',newline='')
        for index,rows in enumerate(file):
            if index == 1:
                row = rows
                profit = row.split(',')  # t+1期的收益
        file.close()
        for day in graduation.Tradedate.Date:
            file = open('F:/毕业设计/std_factor_data/'+str(day) + '.csv', 'r',newline='')
            reader = csv.reader(file)
            factor_row = []
            ticker_row = []
            for index,rows in enumerate(reader):
                if index == 0:
                    ticker_row = rows
            factor_order = ticker_row.index(graduation.Ticker.List[i])
            file.close()
            file = open('F:/毕业设计/std_factor_data/'+str(day) + '.csv', 'r', newline='')
            reader = csv.reader(file)
            for index,rows in enumerate(reader):
                if index == i+1:
                    factor_row = rows
            factor.append(factor_row[factor_order])
            file.close()
        ticker_list = []
        ticker_list.append(ticker)
        data.append(ticker_list)
        data.append(profit)
        data.append(factor[:-1])
    file = open('F:/毕业设计/Section_in_factor/'+str(graduation.Factor_name.List[i]) + '.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerows(data)
