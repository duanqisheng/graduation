'''
# 这一段代码用来提取原始数据的因子名称，并保存
# 这个文件中有有序的因子名称List可以调用
import csv
file = open('F:/毕业设计/merge_original_data_2015_2017.csv', 'r')
reader = csv.reader(file)
List = []
for index, rows in enumerate(reader):
    if index == 0:
        row = rows
for ele in row[4:]:
    List.append(ele)
with open('F:/毕业设计/Factor_name.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerow(List)
print(List)
'''
import csv
file = open('F:/毕业设计/Factor_name.csv', 'r')
reader = csv.reader(file)
List = []
for index, rows in enumerate(reader):
    if index == 0:
        List = rows
# print(List)
