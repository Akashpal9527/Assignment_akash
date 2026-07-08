# 2. Write a program to calculate the sum of all values in the dictionary
def sum_valuse(dic):
    s=0
    for i in dic:
        s+=dic.get(i)
    return s
d = {1: 1, 2: 2, 3: 3, 4: 4}
print(sum_valuse(d))