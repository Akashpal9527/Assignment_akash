# 8. Write a program to extract alternate key-value pairs from the dictionary
def laternate(d):
    ans={}
    l=[]
    l1=[]
    for i in d:
        l.append(i)
        l1.append(d.get(i))
    for j in range(len(l)):
        if j%2==0:
            ans[l[j]]=l1[j]
    return ans
player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
# print(len(player))
print(laternate(player))