import sys,re,collections

WORD_RE = re.compile('\w+')
# index2 = {}
index2=collections.defaultdict(list)
with open(sys.argv[0],encoding='utf-8') as f:
    for line_no,line in enumerate(f,1):
        # print(line_no,line)
        for match in WORD_RE.finditer(line):
            word = match.group()
            # print(word)
            column_no = match.start() + 1
            # print(word, column_no)
            location = (line_no, column_no)
            # print(word,location)
            # print(index2)
            index2[word].append(location)
    print(index2)
    print(type(index2),type(index2['import']))
for word in sorted(index2,key=str.upper):
    print(word,index2[word])
# print(index2['666'])