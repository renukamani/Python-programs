str = "Hi this is renuka, I am an engineer"
str = str.casefold()
vowels = "aeiou"
lst = list()
for character in str :
    if character in vowels :
        lst.append(character)
lst = set(lst)
print(lst)
