# 15. Write a program to remove a specific key (for example, key = 2) from the dictionary
def rem(d,key):
    d1={}
    for i in d:
        if i==key:
            continue
        else:
            d1[i]=d.get(i)
    return d1
d = {1: 10, 2: 20, 3: 30}
print(rem(d,2))