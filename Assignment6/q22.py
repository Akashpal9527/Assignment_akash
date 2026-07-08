# 22. Write a program to update a value in a dictionary if the key exists; otherwise, add the key.
def akash(d,key,val):
    for i in d:
        if i==key:
            d[i]=val
            break
    else:
        d[key]=val
    return d
key=int(input("enter key:"))
val=int(input("enter val:"))
d = {1: 10, 2: 20, 3: 30,4:90,5:56,6:23,7:100}
print(akash(d,key,val))