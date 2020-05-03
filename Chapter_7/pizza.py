class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


# print(Pizza.get_size()) Causes error
print(Pizza.get_size(Pizza(42)))
print(Pizza(42).get_size)
print(Pizza(42).get_size())
m = Pizza(42).get_size
print(m())
print(m.__self__)
print(m == m.__self__.get_size)