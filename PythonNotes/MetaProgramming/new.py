class X:
    def __new__(cls, *args, **kwargs):
        print("__new__", args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("__init__", args, kwargs)


x = X(1, 2, name='falonie')
