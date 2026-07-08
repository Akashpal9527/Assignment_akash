# 23. Write a program to convert two lists into a dictionary Example: keys = [1, 2, 3], values = ["a", "b", "c"]
def list_dict(keys,values):
    d={}
    for i in range(len(keys)):
        d[keys[i]]=values[i]
    return d
keys=[1, 2, 3]
values=["a", "b", "c"]
print(list_dict(keys,values))