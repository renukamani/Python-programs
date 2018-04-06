str = "HI this is is  renukamani92"
str_1 = str.split()
n = len(str_1)
n1 = n -1
for i in range(int(n/2)) :
    temp = str_1[i]
    str_1[i] = str_1[n1]
    str_1[n1] = temp
    n1 = n1-1
print(" ".join(str_1))

str_2 = str_1[::-1]
print(" ".join(str_1))
