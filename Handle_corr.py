import pandas as pd
import csv
import Ticker
import factor_name
factor_corr = []
i = 0
for f_name in factor_name.List:
  factor = []
  for ticker in Ticker.List:
    file = open('C:/Users/Administrator/Desktop/毕业设计/profit/'+str(ticker)+'.csv', 'r')
    profitdata = []
    reader = csv.reader(file)
    for row in reader:
        for ele in row:
            profitdata.append(float(ele))
    #print(profitdata)
    factorfile = open('C:/Users/Administrator/Desktop/毕业设计/factor/'+str(ticker)+'.csv', 'r')
    factordata = []
    reader = csv.reader(factorfile)
    for row in reader:
       factordata.append(float(row[i]))
    # print(factordata)
    s1 = pd.Series(profitdata)
    s2 = pd.Series(factordata)
    corr = s1.corr(s2)
    # print(corr)
    factor.append(corr)
  i += 1
  factor_corr.append(factor)
  with open('C:/Users/Administrator/Desktop/毕业设计/factor_corr/'+str(f_name)+ '.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerow(factor)
print(factor_corr)
print(len(factor_corr))
print(i)
