def mygenerator():
    yield 1
    yield 2
    yield 'a'


print(mygenerator())
g = mygenerator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))