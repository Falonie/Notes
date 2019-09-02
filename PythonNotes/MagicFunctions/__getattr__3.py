class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = f'Value for {item}'
        setattr(self, item, value)
        return value


# data = LazyDB()
# print('Before:', data.__dict__)
# print('foo:', data.foo)
# print('After:', data.__dict__)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, item):
        print(f'Called __getattr__ {item}')
        return super().__getattr__(item=item)


# data = LoggingLazyDB()
# print('exists:', data.exists)
# print('foo:', data.foo)
# print(data.__dict__)

# data = LoggingLazyDB()
# print('before:', data.__dict__)
# print('foo:', data.foo)
# print('foo exists:', hasattr(data, 'foo'))
# print('After:', data.__dict__)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print(f'Called __getattr__ {item}')
        try:
            return super().__getattribute__(item)
        except AttributeError:
            value = f'Value for {item}'
            setattr(self, item, value)
            return value


# data = ValidatingDB()
# print('exists:', data.exists)
# print(data.__dict__)
# print('foo:', data.foo)
# print(data.__dict__)


class SavingDB(object):
    def __setattr__(self, key, value):
        super().__setattr__(key, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, key, value):
        print(f'Called __setattr__ ({key} {value})')
        super().__setattr__(key=key, value=value)


# data = LoggingSavingDB()
# print('before:', data.__dict__)
# data.foo = 5
# print('After:', data.__dict__)
# data.foo = 10
# print('Finally:', data.__dict__)

# data = SavingDB()
# print('before:', data.__dict__)
# data.foo = 5
# print('After:', data.__dict__)
# data.foo = 10
# print('Finally:', data.__dict__)


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        print(f'Called __getattrbute__ {item}')
        return self._data[item]


# data = BrokenDictionaryDB({"foo": 5})
# print(data.foo)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        print(f'Called __getattrbute__ {item}')
        data_dict = super().__getattribute__('_data')
        return data_dict[item]


data = DictionaryDB({"foo": 5})
print(data.foo)
