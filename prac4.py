
def Gen_fib(a) :
    f = list()
    n = 1
    c = 1
    f.append(n)
    f.append(c)
    for i in range(a-2) :
        s = c+n
        f.append(s)
        c = n
        n = s
    print(*f)

inp = input("enter a number")
Gen_fib(int(inp))
