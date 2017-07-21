import re, reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


with open('voa.txt', 'r') as f:
    # for line in f.readlines():
    l = ''.join(line.strip() for line in f.readlines())
    # print(l)
    # print(f.readlines()[0])

if __name__ == '__main__':
    s = Sentence(l)
    print(s)
    # for word in s:
    #     print(word)
    print(list(s))