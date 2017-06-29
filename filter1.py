def fun(n):
    return n % 3 == 0
print(list(filter(lambda x:x%3==0,[1,3,6,7,5,15])))

def is_palindrome(n):
    return int(str(n)[::-1]) == n
output = filter(is_palindrome,range(1,1000))
print(list(output))