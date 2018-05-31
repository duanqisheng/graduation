import graduation.My_function
import graduation.Tradedate
import csv
j = 0
for day in graduation.Tradedate.Date:
    j += 1
    print('第'+str(j)+'天')
    data = []
    factor = []
    with open('F:/毕业设计/del_extreme_factor_data/'+day+'.csv', 'r') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if index == 0:
                ticker = row
    data.append(ticker)
    with open('F:/毕业设计/del_extreme_factor_data/'+day+'.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            factor.append(row)
        factor.remove(ticker)
        for rows in factor:
            for i in range(len(rows)):
                rows[i] = float(rows[i])
            rows = graduation.My_function.standardize(rows)
            data.append(rows)
    with open('F:/毕业设计/std_factor_data/'+day+'.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
