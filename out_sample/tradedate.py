'''
import pandas as pd
import graduation.My_function

file = open('F:/毕业设计/样本外数据/final_factor.csv')
df = pd.read_csv(file,index_col=0)
myset = set()
list = []
for ele in df['tradeDate']:
    myset.add(ele)
for ele in myset:
    list.append(ele)
list = graduation.My_function.sort_date_outsample_func(list)
pd.DataFrame(list).to_csv('F:/毕业设计/样本外数据/date.csv')
print('Date list Load done')
'''
import pandas as pd
file = open('F:/毕业设计/样本外数据/date.csv')
df = pd.read_csv(file,index_col=0,header=0)
list = df['0'].tolist()
print(list)
print('date load done')
