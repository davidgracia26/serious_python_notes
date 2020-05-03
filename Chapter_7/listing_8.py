class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)


print(Pizza().cook is Pizza().cook)
print(Pizza().mix_ingredients is Pizza.mix_ingredients)
print(Pizza().mix_ingredients is Pizza().mix_ingredients)