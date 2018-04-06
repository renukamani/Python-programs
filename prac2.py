a = [1,4,6,2,76,4,6,89,4,7,455,85,67,32]
a = set(a)
b = list()
for i in a :
    if (i%2 == 0) :
        b.append(i)
print(b)
