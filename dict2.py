name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle :
    line = line.strip()
    word = line.split()
    if len(word)<1 :
        continue
    if word[0] is 'From' :
        t = word[5].split(':')
        counts[t[0]] = counts.get(t[0],0)+1
lst=list()
for k,v in counts.items() :
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst :
    print(k,v)
