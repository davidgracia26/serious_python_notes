from unittest import mock


m = mock.Mock()
m.some_method.return_value = 42
m.some_method()
m.some_method("with", "arguments")