# 输出244*244的矩阵
import csv
import Ticker
for ticker in Ticker.List:
    file = open('C:/Users/Administrator/Desktop/毕业设计/data/'+str(ticker)+'.csv', 'r')
    factordata = []
    reader = csv.reader(file)
    for row in reader:
        if row:
            factordata.append(row[4:])

    with open('C:/Users/Administrator/Desktop/毕业设计/factor/'+str(ticker) + '.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        data = []
        for row in factordata:
            for item in row:
                if item == 'nan':
                    item = 0
                    data = row
            writer.writerow(data)
