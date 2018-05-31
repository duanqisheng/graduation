# 这一段用来分割成各个股票独立的csv文件
# 文件大小是732*248的矩阵
# 其中732是2015-2017这732个交易日，248中前四列是股票信息，后244列是因子数据
# 该文件只用执行一次分割即可
import csv
import graduation.Ticker
i = 0
for ticker in graduation.Ticker.List:
    # print('还有' + str(300-i) +'支股票！')
    # print("ticker" + ticker)
    i += 1
    with open('F:/毕业设计/Section_in_Ticker/'+str(ticker) + '.csv', 'w', newline='') as f:
        file = open('F:/毕业设计/merge_original_data_2015_2017.csv', 'r')
        reader = csv.reader(file)
        writer = csv.writer(f)
        for index, rows in enumerate(reader):
            if rows[2] == ticker:
                data = rows
                writer.writerow(data)

