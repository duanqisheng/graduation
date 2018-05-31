a = [1,2,3]
b = [2,3,4]
d = [-1] * 3
for ele in a:
    if ele in b:
        b.remove(ele)
print(d)
