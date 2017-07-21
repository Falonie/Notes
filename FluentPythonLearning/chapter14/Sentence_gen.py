import re, reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        for word in self.words:
            yield word
        return