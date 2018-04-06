num = int(input("enterthe number"))
sq_num = int(num**0.5)
set_flag = "Y"
for i in range(2,sq_num+1) :
    if num % i == 0 :
        print("not prime")
        set_flag = "N"
        break
    else :
        continue
if set_flag != "N" :
    print("prime")
