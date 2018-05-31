import csv
import factor_name
List = []
for name in factor_name.List:
    file = open('C:/Users/Administrator/Desktop/毕业设计/factor_corr/'+name+'.csv', 'r')
    reader = csv.reader(file)
    i = 0
    sum = 0
    for row in reader:
        for ele in row:
            if ele == 'nan':
                pass
            else:
                i += 1
                sum += float(ele)
    factor_avg = sum / i
    List.append(factor_avg)
    print(name)
print(List)
print(len(List))
with open('C:/Users/Administrator/Desktop/毕业设计/factor_corr_avg.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(List)
