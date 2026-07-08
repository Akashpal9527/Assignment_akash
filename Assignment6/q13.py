# 13. Write a program to find the maximum value in the dictionary
def mixi_value(d):
    maxi=-100
    
    for i in d:
        if d.get(i)>maxi:
            maxi=d.get(i)
    return f"maximum value in the dictionary:{maxi}"
marks = {"A": 85, "B": 90, "C": 75, "D": 95}
print(mixi_value(marks))
