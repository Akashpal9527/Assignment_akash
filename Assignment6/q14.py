# 14. Write a program to swap keys and values in the dictionary
def swap_key_val(d):
    new_d={}
    for i  in d:
        new_d[d.get(i)]=i
    return new_d
d = {1: "one", 2: "two", 3: "three"}
print(swap_key_val(d))
