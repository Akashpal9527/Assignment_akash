# 24. Write a program to remove duplicate values from a dictionary
def dupli(d):
    d1={}
    l=[]
    for i in d:
        if d.get(i) not in l:
            l.append(d.get(i))
            d1[i]=d.get(i)
    return d1

d = {1: 10, 2: 20, 3: 30,4:90,5:56,6:56,7:100}
print(dupli(d))