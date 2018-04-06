
# Sample code to perform I/O:

n = input("enter stations")
n = int(n)
c = list()
l = list()
for i in range(n) :
    c.append(int(input("enter the cost of petrol in station")))
    l.append(int(input("enter the petrol amount reqd to reach station")))

i =0
total_cost=0

while i < n-1 :
    litres =0
    litres = litres + l[i]
    for j in range(i+1,n) :
        if c[i] < c[j] :
            litres = litres +l[j]
            if j is n-1 :
                total_cost = total_cost + (litres * c[i])
                i = j
                break
        else :
            total_cost = total_cost + (litres * c[i])
            i = j
            if i is n-1 :
                litres = l[i]
                total_cost = total_cost + (litres * c[i])
            break
print(total_cost)





# Write your code here
