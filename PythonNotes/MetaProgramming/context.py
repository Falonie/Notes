class Manager(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = 'It has {}'.format(self.text)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = 'Done.'


with Manager("time") as f:
    print(f.text)
