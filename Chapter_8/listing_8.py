import operator
from functools import partial
from first import first


def greater_than(number, min=0):
    return number > min


mylist = [-1, 0, 1, 2]

print(first(mylist, key=partial(greater_than, min=42)))
print(first(mylist, key=partial(operator.le, 0)))

