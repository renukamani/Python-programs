lst = ["a", "b", "b", "c", "a"]
lst1 = list()
lst2 = set(lst)
print(lst2)
for item in lst2 :
    if lst.count(item) > 1 :
        n = lst.count(item) - 1
        for i in range(n) :
            lst1.append(item)
    else :
        continue
print(lst1)
