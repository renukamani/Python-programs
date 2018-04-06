names = ["kjscahj","jgsgascg","jhvkumar","praveenkumar"]
for item in names:
    item = item.casefold()
    if item.find("kumar") >= 0 :
        names.remove(item)
print(names)
