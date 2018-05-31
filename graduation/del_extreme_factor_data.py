'''
# 只用执行一次
# 清洗因子数据，去掉极值，并保存
import graduation.My_function
import graduation.Tradedate
import csv
j = 0
for day in graduation.Tradedate.Date:
    j += 1
    print('第'+str(j)+'天')
    data = []
    with open('F:/毕业设计/Section_in_date/'+day+'.csv','r') as file:
        reader = csv.reader(file)
        ticker = [row[0] for row in reader]
    data.append(ticker)
    for i in range(244):
        with open('F:/毕业设计/Section_in_date/'+day+'.csv','r') as file:
            reader = csv.reader(file)
            factor = [row[2+i] for row in reader]
            for i in range(len(factor)):
                if factor[i] == 'nan':
                    factor[i] = 0
                else:
                    factor[i] = float(factor[i])
            factor_1 = graduation.My_function.del_extreme(factor)
            factor_2 = graduation.My_function.del_extreme(factor_1)
            factor_3 = graduation.My_function.del_extreme(factor_2)
        data.append(factor_3)
    with open('F:/毕业设计/del_extreme_factor_data/'+day+'.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
'''
