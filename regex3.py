import re

text = 'Hello world! Hello China!'
print(text.replace('world', 'Python'))
print(re.sub(r'world', 'Python', text))
pattern = re.compile('world')
print(pattern.sub('Python', text))
print(pattern.search(text).group())
print(re.match(r'Hello', text).group())
p=re.search(r'\A(.*?)\s',text)
print(p.groups(),p.group())
# p.group()
if __name__ == '__main__':
    pass