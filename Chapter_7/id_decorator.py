def identity(f):
    return f


@identity
def foo():
    return 'bar'

# is equivalent to


def foo():
    return 'bar'


foo = identity(foo)