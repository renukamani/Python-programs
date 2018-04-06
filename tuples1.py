fhand = open('test.txt')
counts = dict()
for line in fhand :
    line = line.strip()
    if len(line) < 1 :
        continue
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for k,v in counts.items() :
    lst.append((v,k))
lst = sorted(lst,reverse=True)

for val,key in lst[:10] :
    print(key,val)

print(sorted([(v,k) for k,v in counts.items()]))
