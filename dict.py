counts=dict()
names = ["hi","hello","hola","namaste","namaste","hi","hi"]
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)
