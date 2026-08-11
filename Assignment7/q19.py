# 19. Write a function to find the most repeated character in a string.
def repeated(str1):
    d={}
    for i in str1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    larg=-100
    l=[]
    for i in d:
        if d.get(i)>larg:
            larg=d.get(i)
            l.append(i)
    return l[-1]

str1="Write a function to find the most repeated character in a string tttttttt"
print(repeated(str1))

