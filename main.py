def add_sprinkles(func):
    def wrapper(args, **kwargs):
        print("before")
        func(args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(args, **kwargs):
        print("you add fudge")
        func(args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"here is your icecream {flavour}")


get_ice_cream("burberry")