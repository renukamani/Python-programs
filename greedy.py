import re
x = "From: using the :  character"
y = re.findall("^F.+:",x) #takes the largest string if more than one is matching
print(y)
y = re.findall("^F\S+:",x)
print(y)
y = re.findall("^F.+?:",x) #"?" signifies dont be greedy
print(y)

x = "From renukamani92@gmail.com Sat Jan 5 09:14:18 2008"
y = re.findall("\S+@\S+",x)
print(y)
y = re.findall("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]",x)
print(y)
y = re.findall("\S+@\S+?",x)
print(y)
y = re.findall("^From.*?(\S+@\S+)",x) #paranthese specify what needs to be extracted
print(y)
y = re.findall("@([^ ]*)",x)
print(y)
y = re.findall("\S+?@\S+",x)
print(y)
