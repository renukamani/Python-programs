def takeSecond(elem) :
    return elem[1]

age = dict()

while True :
    name = input("enter persons name:")
    if len(name) < 1 :
        break
    yrs = int(input("enter age"))
    age[name] = yrs

age_list = list(age.items())

age_list.sort(key=takeSecond)

print("sorted:",age_list)

for item in age_list :
    if int(item[1]) > 18 :
        continue
    else :
        print("less than 18:",item)
        age_list.remove(item)

print(age_list)
