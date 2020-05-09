import attr


@attr.s
class Car(object):
    color = attr.ib(converter=str)
    speed = attr.ib(default=0)

    @speed.validator
    def speed_validator(self, attribute, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
