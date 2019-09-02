class Word(object):
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __repr__(self):
        return f"Word {self.text}"


word = Word('python')
word2 = Word('PYTHON')
# print(word2)
print(word == word2)
print()


class Number(object):
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __le__(self, other):
        return self.num <= other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __add__(self, other):
        return self.num + other.num

    def __mod__(self, other):
        return self.num % other.num

    def __repr__(self):
        return f"Num {self.num} {self.__class__.__name__}"

    def __call__(self, *args, **kwargs):
        return f"Num {self.num} {self.__class__.__name__}"



num = Number(4)
num2 = Number(10)
print(num2)
print(num2())
print(num == num2)
print(num2 >= num)
print(num <= num2)
print(num + num2)
print(num2 % num)
