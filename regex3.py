import re

text='Hello world!'
print(text.replace('world','Python'))
print(re.sub(r'world','Python',text))
pattern=re.compile('world')
print(pattern.sub('Python',text))
print(pattern.search(text).group())
print(re.match(r'Hello',text).group())