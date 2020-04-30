import warnings


class Car(object):
    """A representation of a car."""
    def turn_left(self):
        """Turn the car left.

        ..deprecated:: 1.1
          Use :func:`turn` instead with the direction argument set to "left".
        """
        warnings.warn("turn_left is deprecated; use turn instead", DeprecationWarning)
        self.turn(direction='left')

    def turn(self, direction):
        """Turn the car in some direction.

        :param direction: The direction to turn to.
        :type direction: str
        """
        # Write actual code here instead
        pass

# from debtcollector import moves
#
#
# class Car(object):
#     """A representation of a car."""
#
#     @moves.moved_method('turn', version='1.1')
#     def turn_left(self):
#         """Turn the car left."""
#         self.turn(direction='left')
#
#     def turn(self, direction):
#         """Turn the car in some direction.
#
#         :param direction: The direction to turn to.
#         :type direction: str
#         """
#         # Write actual code here instead
#         pass