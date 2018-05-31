import graduation.Tradedate
import graduation.Ticker
import csv
import graduation.My_function
import pandas as pd
import numpy as np


def ass_profit(list):
    ass_profit_list = []
    for i in range(len(graduation.Tradedate.Date)):
        print('第'+str(i)+'天!')
        ass_profit_list.append(0)
        for ticker in graduation.Ticker.com_List:
            with open('F:/毕业设计/profit/' + ticker + '.csv', 'r') as f:
                reader = csv.reader(f)
                for index, rows in enumerate(reader):
                    if index == 1:
                        row = rows
                while(True):
                    if len(row) < len(graduation.Tradedate.Date):
                        row.append(0)
                    else:
                        break
                ass_profit_list[i] += float(row[i] * list[i])
                ass_profit_list[i] /= 300
    return ass_profit_list


def group_profit(list):
    file = open('F:/毕业设计/Section_in_time_profit.csv', 'r')
    df = pd.read_csv(file,header=0,index_col=0)
    data = []
    for i in list:
        data.append(df.iloc[i])
    group_p = pd.DataFrame(data)
    return group_p.mean(axis=0).tolist()


def group_profit_for_dayi(list,i):
    file = open('F:/毕业设计/Section_in_time_profit_indexisticker.csv', 'r')
    df = pd.read_csv(file,header=0,index_col=0)
    data = []
    for j in list:
        data.append(df.loc[j][i+1])
    group_p_dayi = np.array(data)
    return group_p_dayi.mean()


def group_profit_for_dayi_impack(list,i,oldlist,impack):
    file = open('F:/毕业设计/Section_in_time_profit_indexisticker.csv', 'r')
    df = pd.read_csv(file,header=0,index_col=0)
    data = []
    adjust = [impack] * len(list)
    for k in range(len(list)):
        if list[k] in oldlist:
            adjust[k] = 0
    for j in range(len(list)):
        data.append(df.loc[list[j]][i+1]+adjust[j])
    group_p_dayi = np.array(data)
    return group_p_dayi.mean()
