# 20. Write a program to count how many values are greater than 50 in a dictionary.
def akash(d):
    count=0
    for i in d:
        if d.get(i)>50:
            count+=1
    return count
d = {1: 10, 2: 20, 3: 30,4:90,5:56,6:23,7:100}
print(akash(d))