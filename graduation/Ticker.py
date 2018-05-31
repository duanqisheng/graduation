'''
# 这一段是用来从原始数据集中提取所有股票的代码，组成set集合，构成股票组合的代码。
# 该文件下有无序的Ticker列表可以使用，调用的方式使List。
# 另外还有补全六位的ticker列表，调用方式使com_List。
# 共有300只股票
import csv
import pandas as pd
file = open('F:/毕业设计/merge_original_data_2015_2017.csv', 'r')
df = pd.read_csv(file)

with open('F:/毕业设计/Ticker_number.csv', 'w') as f:
     writer = csv.writer(f)
     Set = set()
     for index, row in df.iterrows():
         Set.add(row['ticker'])
     writer.writerow(Set)
'''
import csv
import graduation.My_function
# 读取股票代码。并组成List
List = list()
com_List = list()
file = open('F:/毕业设计/Ticker_number.csv', 'r')
reader = csv.reader(file)
for index,rows in enumerate(reader):
    if index == 0:
        List = rows
com_List= graduation.My_function.Complet_ticker(List)
# print(List) # 打印观察List是否正确
# 该股票代码的List是无序的
# print(com_List)
