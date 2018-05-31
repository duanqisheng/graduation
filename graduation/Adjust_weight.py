import graduation.Create_factor_ass_data
import pandas as pd
import graduation.Factor_name

file = open('F:/毕业设计/factor_evalute.csv','r')
df = pd.read_csv(file)
adjust_weight_coe = list()
for ele in df['IR']:
    if float(ele)>0:
        adjust_weight_coe.append(1)
    else:
        adjust_weight_coe.append(-1)
print(adjust_weight_coe)
for i in range(len(adjust_weight_coe)):
    print(graduation.Factor_name.List[i])
    if adjust_weight_coe[i] > 0:
        adjust_weight_df = graduation.Create_factor_ass_data.d[graduation.Factor_name.List[i]].df
    else:
        adjust_weight_df = (graduation.Create_factor_ass_data.d[graduation.Factor_name.List[i]].df-2).__abs__()
    adjust_weight_df.to_csv('F:/毕业设计/Adjust_factor_ass_weight/'+str(graduation.Factor_name.List[i]) + '.csv')

