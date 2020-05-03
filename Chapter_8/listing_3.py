import inspect


def mygenerator():
    yield 1


print(inspect.isgeneratorfunction(mygenerator))
print(inspect.isgeneratorfunction(sum))