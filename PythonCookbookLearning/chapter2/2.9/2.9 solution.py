import unicodedata

s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
print(s1,s2,s1==s2,len(s1),s2.__len__())

t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
t3=unicodedata.normalize('NFC','www.salesmind.cn/\xa0')
print(t1,t2,t1==t2,t3)
print(unicodedata.normalize('NFC','https://www.antfin.com/\xa0'))