import re
import numpy as np


def sort_date_func(date):
    patt = '(\d+)_(\d+)_(\d+)'
    for i in range(len(date)-1):
        for x in range(i+1, len(date)):
            j = 1
            while j < 4:
                lower = re.match(patt, date[i]).group(j)
                upper = re.match(patt, date[x]).group(j)
                # print lower,upper
                if int(lower) < int(upper):
                    j = 4
                elif int(lower) == int(upper):
                    j += 1
                else:
                    date[i], date[x] = date[x], date[i]
                    j = 4
    return date


def sort_date_outsample_func(date):
    patt = '(\d+)-(\d+)-(\d+)'
    for i in range(len(date)-1):
        for x in range(i+1, len(date)):
            j = 1
            while j < 4:
                lower = re.match(patt, date[i]).group(j)
                upper = re.match(patt, date[x]).group(j)
                # print lower,upper
                if int(lower) < int(upper):
                    j = 4
                elif int(lower) == int(upper):
                    j += 1
                else:
                    date[i], date[x] = date[x], date[i]
                    j = 4
    return date

def Complet_ticker(list):
    complet_list = []
    for i in range(len(list)):
        complet_list.append(0)
    patt_1 = re.compile(r'[0-9]{1}')
    patt_2 = re.compile(r'[0-9]{2}')
    patt_3 = re.compile(r'[0-9]{3}')
    patt_4 = re.compile(r'[0-9]{4}')
    patt_5 = re.compile(r'[0-9]{5}')
    patt_6 = re.compile(r'[0-9]{6}')
    for i in range(len(list)):
        if re.match(patt_6, list[i]):
            complet_list[i] = list[i]
        elif re.match(patt_5,list[i]):
            complet_list[i] = '0'+list[i]
        elif re.match(patt_4,list[i]):
            complet_list[i] = '00'+list[i]
        elif re.match(patt_3,list[i]):
            complet_list[i] = '000'+list[i]
        elif re.match(patt_2,list[i]):
            complet_list[i] = '0000'+list[i]
        else:
            complet_list[i] = '00000'+list[i]
    return complet_list


def del_extreme(list):
    array = np.asarray(list, dtype=float)
    sigma = array.std()
    mean = array.mean()
    array[array > mean+3*sigma] = mean + 3*sigma
    array[array < mean-3*sigma] = mean - 3*sigma
    return array


def standardize(list):
    array = np.asarray(list)
    sigma = array.std()
    mean = array.mean()
    array -= mean
    array /= sigma
    return array


def correlation_coefficent(list1,list2):
    array1 = np.asarray(list1)
    array2 = np.asarray(list2)
    corr = np.corrcoef(array1,array2)
    return corr[0][1]


def compute_accumulated_profit(list):
    netvalue = 1
    for ele in list:
        netvalue *= 1 + ele/100
    return (netvalue-1)*100


def compute_accumulated_market_profit(list):
    netvalue = 1
    for ele in list:
        netvalue *= 1 + ele
    return (netvalue-1)*100


def compute_annual_profit(list):
    accumulated_profit = compute_accumulated_profit(list)
    return (pow((accumulated_profit/100+1),1/3)-1)*100


def excess_profit(list,marker_list):
    return compute_accumulated_profit(list)-compute_accumulated_market_profit(marker_list)


def compute_IR(list):
    accumulated_profit = compute_accumulated_profit(list)
    array = np.asarray(list)
    std = array.std()
    return accumulated_profit/std

def compute_probability_win(list,market_list):
    j = 0
    for i in range(len(list)):
        if list[i]>market_list[i]:
            j += 1
    return j/len(list)
