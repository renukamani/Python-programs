counts = dict()
fname = input("enter the file name")
fh = open (fname)
for line in fh :
    words = line.split()
    for word in words :
        word = word.lower()
        counts[word] = counts.get(word,0) + 1
print("total",counts)
bigCount = None
bigWord = None
for word,count in counts.items() :
    if bigCount is None or count > bigCount :
        bigWord = word
        bigCount = count
print(bigWord,bigCount)
