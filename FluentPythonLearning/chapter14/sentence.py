import re, reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))


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
    print(s[10])