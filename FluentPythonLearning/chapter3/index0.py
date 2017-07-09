import sys
import re

WORD_RE = re.compile('\w+')
index,index2 = {},{}
with open(sys.argv[0],encoding='utf-8') as f:
    for line_no,line in enumerate(f,1):
        # print(line_no,line)
        for match in WORD_RE.finditer(line):
            word = match.group()
            # print(word)
            column_no = match.start() + 1
            # print(word, column_no)
            location = (line_no, column_no)
            # print(word)
            occurrences2 = index2.get(word, [])
            occurrences2.append(location)
            index['word']=occurrences2
print(index)
# for key,value in index.items():
#     print(key,value)
for word in sorted(index,key=str.upper):
    print(word, index['word'])