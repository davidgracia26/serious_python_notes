x = []
for i in (1, 2, 3):
    x.append(i)

print(x)

x = [i for i in (1, 2, 3)]
print(x)

x = [word.capitalize()
     for line in ("hello world?", "world!", "or not")
     for word in line.split()
     if not word.startswith("or")]
print(x)

y = {x: x.upper() for x in ['hello', 'world']}
print(y)