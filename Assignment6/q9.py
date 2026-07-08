# 9. Write a program to find all values that start with the letter ‘K’
def letter_with_K(d):
    l=[]
    for i in d:
        a=d.get(i)
        if a[0]=="K":
            l.append(d.get(i))
    return l
player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
print(letter_with_K(player))