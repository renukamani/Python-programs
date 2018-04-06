import re
num = list()
sum1 = 0
fh = open("actual1.txt")
for line in fh :
    line = line.strip()
    if len(line) < 1 :
        continue
    nums = re.findall("[0-9]+",line)
    for num in nums :
        num = int(num)
        sum1 = sum1 + num
print(sum1)
