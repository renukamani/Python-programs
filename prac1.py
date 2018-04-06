str = input("enter string")
l = len(str) - 1
for i in range(len(str)) :
    if i == l :
        print ("palindrome")
    if str[i] == str[l] :
        l = l-1
        continue
    else :
        break
