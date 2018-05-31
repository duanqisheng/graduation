import pandas as pd
a = [[1,2,3],
    [1,-1,3],
    [1,3,3]]

b = pd.DataFrame(a)

print(b.sort_values(by=1))

mystr = 'duanduanduan'
print(mystr.upper())
