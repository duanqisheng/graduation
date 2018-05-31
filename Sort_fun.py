def max_fac(list):
    newlist = []
    for num in range(1,11):
        newlist.append(list.index(sorted(list)[-num]))
    return newlist


def min_fac(list):
    newlist = []
    for num in range(10):
        newlist.append(list.index(sorted(list)[num]))
    return newlist


def average(list):
    count = 0
    total = 0
    for ele in list:
        total += ele
        count += 1
    return total/count
