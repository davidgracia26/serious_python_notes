a = map(lambda x: x + "bzz!", ["I think", "I'm good"])
print(a)
print(list(a))

b = (x + "bzz!" for x in ["I think", "I'm good"])
print(b)
c = [x + "bzz!" for x in ["I think", "I'm good"]]
print(c)

d = filter(lambda x: x.startswith("I "), ["I think", "I'm good"])
print(d)
print(list(d))

e = (x for x in ["I think", "I'm good"] if x.startswith("I "))
print(e)
print(list(e))

for i, item in enumerate(['one', 'two']):
    print("Item %d: %s" % (i, item))

mylist = [("a", 2), ("c", 1), ("d", 4)]
print(sorted(mylist))
print(sorted(mylist, key=lambda x: x[1]))

mylist = [0, 1, 3, -1]
if all(map(lambda x: x > 0, mylist)):
    print("All items are greater than 0")
if any(map(lambda x: x > 0, mylist)):
    print("At least one item is greater than 0")

keys = ["foobar", "barzz", "ba!"]
print(zip(keys, map(len, keys)))
print(list(zip(keys, map(len, keys))))
print(dict(zip(keys, map(len, keys))))