class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

import re

s = "I love you, regardless."
line = 'adasda;dasda , weqewq, foooo.'
pattern = re.compile(r'(,|.)\s*')
# print(pattern.split(s))
# print(re.split(r'(,|.|\s)\s*',s))
print(re.split(r'[;.\s]\s*', line))
print(re.split(r'(;|,|.|\s)\s*', line))
pattern2 = re.compile(r'(;|,|\s)\s*')
print(re.split(r'(;|,|\s)\s*', s))
print(pattern2.split(s))
