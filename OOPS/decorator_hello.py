
def to_upper(func):
    def inner(x):
        func(x.upper())
    return inner

@to_upper
def func(x):
    print(f"Hello {x}")


func("shalini")