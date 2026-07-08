# 1. Write a program to calculate the sum of all keys in the dictionary d = {1: 1, 2: 2, 3: 3, 4: 4}
def sum_keys(dic):
    s=0
    for i in dic:
        s+=i
    return s
dic = {1: 1, 2: 2, 3: 3, 4: 4}
print(sum_keys(dic))