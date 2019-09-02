class Proxy:
    def __init__(self, obj):
        self.obj = obj
        # self.obj = f'__{obj}__'
        # self.__obj = obj
        # self._obj = obj

    def __getattribute__(self, item):
        # return getattr(self, item)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # if key.startswith('_'):
        #     super().__setattr__(key, value)
        # else:
        #     setattr(self, key, value)
        # setattr(self.__obj, key, value)
        # setattr(self._obj, key, value)
        self.__dict__[key] = value


p = Proxy('falonie')
# print(p._obj__Proxy)
# print(p._Proxy__obj)
print(p.obj)
