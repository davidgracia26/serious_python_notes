def check_user_is_not(username):
    def user_check_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == username:
                raise Exception("This user is not allowed to get food")
            return f(*args, **kwargs)
        return wrapper
    return user_check_decorator


class Store(object):
    @check_user_is_not("admin")
    @check_user_is_not("user123")
    def get_food(self, username, food):
        return self.storage.get(food)

# is equivalent to


class Store(object):
    def get_food(self, username, food):
        return self.storage.get(food)


Store.get_food = check_user_is_not("user123")(Store.get_food)
Store.get_food = check_user_is_not("admin")(Store.get_food)