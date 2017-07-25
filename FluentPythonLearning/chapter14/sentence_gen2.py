import re, reprlib

RE_WORD = re.compile('\w')


class Sentence(object):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

with open('voa.txt', 'r') as f:
    # for line in f.readlines():
    l = ''.join(line.strip() for line in f.readlines())
    # print(l)

if __name__ == '__main__':
    print(Sentence(l))