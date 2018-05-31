import csv
import Ticker
import factor_name
import TradeDate
import Sort_fun
factor_avg_file = open('C:/Users/Administrator/Desktop/毕业设计/factor_corr_avg.csv', 'r')
fac_coe = []
fac_coe_reader = csv.reader(factor_avg_file)
for index,rows in enumerate(fac_coe_reader):
    if index == 0:
        row = rows
for ele in row:
    if float(ele) > 0:
        fac_coe.append(1)
    else:
        fac_coe.append(-1)
# print(fac_coe)

for day in TradeDate.List:
    newdate = ''
    for ele in day:
        if ele.isdigit():
            newdate += ele
        else:
            newdate += '_'
    mylist_sort = []
    for j in range(48):
        mylist_sort.append(0)
    for i in range(243):
        mylist = []
        file = open('C:/Users/Administrator/Desktop/毕业设计/Date/'+str(newdate)+'.csv', 'r')
        reader = csv.reader(file)
        count_avg = []
        for rows in reader:
            if rows[i+2] == 'nan':
                mylist.append(0)
            else:
                mylist.append(float(rows[i+2]))
                count_avg.append(float(rows[i+2]))
        for k in range(len(mylist)):
            if mylist[k] == 0:
                mylist[k] = Sort_fun.average(count_avg)
        # print(mylist_sort)
        if fac_coe[i] > 0:
            for ele in Sort_fun.max_fac(mylist):
                mylist_sort[ele] += 1
        else:
            for ele in Sort_fun.min_fac(mylist):
                mylist_sort[ele] += 1
    with open('C:/Users/Administrator/Desktop/毕业设计/factor_sort/'+str(newdate)+ '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(mylist_sort)

