import abc


class BasePizza(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_ingredients(self):
        """Returns the ingredient list."""
        pass


class Calzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]


class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None