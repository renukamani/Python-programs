a = [1,3,5,7,3,6,2,5,7]
b = [5,3,6,7,1,4,7,9,4,5,3,6,8,2,1]
ua = set(a)
ub = set(b)
dup1  = list()
for i in ua :
    if i in ub :
        dup1.append(i)
print(dup1)
