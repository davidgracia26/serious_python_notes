import attr


@attr.s
class Car(object):
    color = attr.ib()
    speed = attr.ib(default=0)