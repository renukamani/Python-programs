def check_armstrong(n) :
    while n > 0:
        sum = 0
        num = n
        p = len(str(n))
        if p == 1 :
            break
        while num > 0 :
            tmp = num % 10
            sum = sum + tmp**p
            num = int(num/10)
        if sum == n :
                print(n)
        n = n-1
check_armstrong(int(input("enter a number below which u want to find the armstrong numbers")))
