class Descriptor(object):
    def __set_name__(self, owner, name):
        print(f'name: {owner.__name__}.{name}')
        self.name = f"__{name}__"

    def __get__(self, instance, owner):
        print(f"get:{instance},{owner}")
        # getattr(instance, self.name, default=None)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"set: {instance}, {value}")
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"del: {instance}")
        raise AttributeError("delete is disabled.")


class X:
    data = Descriptor()


# x = X()
# x.data = 100
# print(x.data)
# del x.data

# d = Descriptor()
# d.data = 10
# print(d.data)


class IntField:
    def __set_name__(self, owner, name):
        self.name = name
        # self.name = f"__{name}__"

    def __get__(self, instance, owner):
        print(f"get:{instance},{owner}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting interger in {self.name}')
        print(f"set: {instance}, {value}")
        instance.__dict__[self.name] = value
        # setattr(instance, self.name, value)


class Model:
    int_field = IntField()


model = Model()
model.int_field = 20
print(model.int_field)
