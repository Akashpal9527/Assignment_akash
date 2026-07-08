# 18. Write a program to find the total number of items in the dictionary
def total(d): 
    count=0
    for i  in d:
        count+=1
    return count
d = {"apple": 5, "banana": 7, "cherry": 3}
print(total(d))