class Function(object):

    def __init__(self,values=None):
        if values is None:
            self.values=[]
        else:
            self.values=values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key]=value

    def __delitem__(self, key):
        del self.values[key]

print(Function({'name':'caren'}))