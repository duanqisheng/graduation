# 分为5组 每组59支股票
# 超配比例为分别为60%，30%，1，-30%，-60%
import pandas as pd
import graduation.Create_factor_data


for factor_name in graduation.Factor_name.List:
    Super_match_wight = 0.3
    one_day_weight = list([1]*295)  # 732*295矩阵
    ass_weight = [one_day_weight]*732
    print(factor_name)
    df = graduation.Create_factor_data.d[factor_name].df
    order = graduation.Create_factor_data.d[factor_name].order
    dd = pd.DataFrame(ass_weight)
    for i in range(732):
        for ele in order[i][0:59]:
            dd.ix[i,ele] = 1+Super_match_wight*2
        for ele in order[i][59:59*2]:
            dd.ix[i,ele] = 1+Super_match_wight*1
        for ele in order[i][59*3:59*4]:
            dd.ix[i,ele] = 1-Super_match_wight*1
        for ele in order[i][59*4:59*5]:
            dd.ix[i,ele] = 1-Super_match_wight*2
    dd.to_csv('F:/毕业设计/factor_ass_weight/'+str(factor_name) + '.csv')
