'''
# 下面是从原始数据集中提取有序交易日期，并且保存到，F:/毕业设计/TrateDate.csv中的代码
# 该文件下有有序的Date序列可以用，类型是list()。
# 三年共有732日交易日
import csv
import pandas as pd
import re
import graduation.My_function
# 提取日期
file2 = open('F:/毕业设计/merge_original_data_2015_2017.csv', 'r')
df = pd.read_csv(file2)
Set = set()
for index, row in df.iterrows():
    Set.add(row['tradeDate'])
List = []
for ele in Set:
    List.append(ele)
# print(len(List))
# 此时日期是无序也是无序的
Date = []
Date2015 = []
Date2016 = []
Date2017 = []
# 更改日期格式
for Day in List:
    newdate = ''
    for ele in Day:
        if ele.isdigit():
            newdate += ele
        else:
            newdate += '_'
    Date.append(newdate)
# print(Date)
# 按年份分别排序，然后连接合并
patt = '(\d+)_(\d+)_(\d+)'
for i in range(len(Date)):
    if re.match(patt, Date[i]).group(3) == '2015':
        Date2015.append(Date[i])
    if re.match(patt, Date[i]).group(3) == '2016':
        Date2016.append(Date[i])
    if re.match(patt, Date[i]).group(3) == '2017':
        Date2017.append(Date[i])
Sort_Date2015 = graduation.My_function.sort_date_func(Date2015)
Sort_Date2016 = graduation.My_function.sort_date_func(Date2016)
Sort_Date2017 = graduation.My_function.sort_date_func(Date2017)
Sort_Date = []
Sort_Date.extend(Sort_Date2015)
Sort_Date.extend(Sort_Date2016)
Sort_Date.extend(Sort_Date2017)
# print(Sort_Date)
# 写入数据
with open('F:/毕业设计/TrateDate.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerow(Sort_Date)
# print(len(Sort_Date))
'''
import csv
file = open('F:/毕业设计/TrateDate.csv', 'r')
reader = csv.reader(file)
for index, rows in enumerate(reader):
    if index == 0:
        row = rows
Date = list()
for ele in row:
    Date.append(ele)
# print(Date)
# print(len(Date))
