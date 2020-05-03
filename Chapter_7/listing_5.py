import functools

from .store import check_is_admin


def foobar(username="someone"):
    """Do crazy stuff"""
    pass


foobar = functools.update_wrapper(check_is_admin, foobar)
print(foobar.__name__)
print(foobar.__doc__)