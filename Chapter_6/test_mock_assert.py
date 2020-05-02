from unittest import mock


m = mock.Mock()
m.some_method("foo", "bar")
m.some_method.assert_called_once_with('foo', 'bar')
m.some_method.assert_called_once_with('foo', mock.ANY)
m.some_method.assert_called_once_with('foo', 'baz')