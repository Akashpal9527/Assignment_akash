# 11. Write a program to check whether a given key exists in the dictionary
def akash(d,key):
    for i in d:
        if i==key:
            return "key exists"
    else:
        return "key not exists"
d = {1: 100, 2: 200, 3: 300}
key=int(input("enter key:"))
print(akash(d,key))