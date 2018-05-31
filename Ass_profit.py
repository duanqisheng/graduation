import Sort_date
import Sort_fun
import csv
import Ticker

Ass_profit = []
i = 0
for day in Sort_date.Date:
    todayprofit_order = []
    todayprofit = []
    file = open('C:/Users/Administrator/Desktop/毕业设计/factor_sort/'+str(day)+'.csv', 'r')
    reader = csv.reader(file)
    for index,rows in enumerate(reader):
        if index == 0:
            row = rows
    todayprofit_order = Sort_fun.max_fac(row)
    # print(todayprofit_order)
    for num in todayprofit_order:
        order = Ticker.List[num]
        profit_file = open('C:/Users/Administrator/Desktop/毕业设计/profit/'+str(order)+'.csv', 'r')
        reader = csv.reader(profit_file)
        for index,rows in enumerate(reader):
            if index == 0:
                row = rows
        todayprofit.append(float(row[i]))
    # print(todayprofit)
    if i < 242:
        i += 1
    Ass_profit.append(Sort_fun.average(todayprofit))
    # print(Sort_fun.average(todayprofit))
# print(Ass_profit)
with open('C:/Users/Administrator/Desktop/毕业设计/Ass_profit.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(Ass_profit)

value = []
origin = 1
for profit in Ass_profit:
    origin *= (1+profit/100)
    value.append(origin)
    print(origin)
    with open('C:/Users/Administrator/Desktop/毕业设计/Ass_value.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(value)
