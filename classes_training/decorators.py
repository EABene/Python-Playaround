# write a program that orders ice cream and uses decorators to add stuff to the ice cream


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("AND Sprinkles are added")
    return wrapper

def add_smarties(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("AND Smarties are added")
    return wrapper


@add_smarties
@add_sprinkles
def get_ice_cream(flavor):
    print(f"You get {flavor} Ice Cream!")


# ----------------------------------------

get_ice_cream("Strawberry")
print()
get_ice_cream("Vanilla")
print()
