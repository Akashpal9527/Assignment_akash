# 10. Write a program to merge two dictionaries
def merge(d1,d2):
    for i  in d2:
        d1[i]=d2.get(i)
    return d1
d1 = {1: "a", 2: "b"}
d2 = {3: "c", 4: "d"}
print(merge(d1,d2))