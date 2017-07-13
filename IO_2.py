import re

filename = 'E:\Trump\'s Attacks on News Media Provoke Backlash.txt'
pattern = re.compile('Trump')

with open(filename) as f:
    for lines in f:
        m = pattern.search(lines)
        if m is not None:
            print(m.group(0))
        else:
            pass