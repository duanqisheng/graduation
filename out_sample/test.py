import pandas as pd
file = open('F:/毕业设计/样本外数据/Section_in_date/第'+str(0)+ '天.csv')
df = pd.read_csv(file,header=None,index_col=0)
dd = pd.DataFrame(df,index=df[10])
print(dd)
print(df)
