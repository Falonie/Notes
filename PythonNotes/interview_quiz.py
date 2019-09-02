class A(object):
    def __init__(self, a, b,c):
        self.__a = a
        self.__b = b
        self._c=c

    # def myprint(self):
    #     print(self.__a, self.__b)
    def __call__(self, *args, **kwargs):
        print(self.__a, self.__b,self._c)



a = A(10, 20,40)
# a.myprint()
a()
print(a._A__a)
print(a._c)
