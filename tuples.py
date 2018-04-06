dict = {'a':2,'b':5,'c':7}
l = list()
for k,v in dict.items() :
    l.append((v,k))
l = sorted(l)
print(l)

print(sorted(dict.items(),reverse = True))
