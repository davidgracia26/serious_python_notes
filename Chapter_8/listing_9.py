import itertools
import operator

a = [{'foo': 'bar'}, {'foo': 'bar', 'x': 42}, {'foo': 'baz', 'y': 43}]
b = list(itertools.groupby(a, operator.itemgetter('foo')))
print(b)
c = [(key, list(group)) for key, group in itertools.groupby(a, operator.itemgetter('foo'))]
print(c)