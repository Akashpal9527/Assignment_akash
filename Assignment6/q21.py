# 21. Write a program to find the key with the highest value in a dictionary
def mixi_value(d):
    maxi=-100
    l=[]
    for i in d:
        if d.get(i)>maxi:
            maxi=d.get(i)
            l.append(i)
    return f"key with maximum value in the dictionary:{l[-1]}"
marks = {"A": 85, "B": 90, "C": 75, "D": 95}
print(mixi_value(marks))