# num=int(input('please input number:'))
# print(len(str(num)))
# print(str(num)[:3])
import itertools

def number(num):
    lengh = len(str(num))
    list = []
    for i in range(1, lengh):
        left_num = int(str(num)[:i])
        right_num = int(str(num)[i:])
        product = left_num * right_num
        list.append(product)
    # list = [l * r for l in left_num for r in right_num]
        #print(product)
    return max(list)

#number(2333)
print(number(2333))
print(max([2,5,9,0,10]))
print([4,5,2,12,4,5,4].count(4))