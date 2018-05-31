import pandas as pd

a =[[1,2,3],[4,6,8],[3,2,1]]
b = pd.DataFrame(a)
print(b)
print(b.sort_values(2))
