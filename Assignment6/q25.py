# 25. Write a program to check whether all values in a dictionary are unique.
def unique(d):
    l=[]
    for i in d:
        if d.get(i) not in l:
            l.append(d.get(i))
        else:
            return "not unique"
    return "unique"
d={1: 10, 2: 20, 3: 30,4:90,5:56,6:57,7:100}
print(unique(d))
