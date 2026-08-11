# 15. Write a function to count capital and small letters in a string
def cap_small(str1):
    cap_count=0
    small_count=0
    for i in str1:
        if i.isupper():
            cap_count+=1
        if i.islower():
            small_count+=1
    return F"no of Capital letters is {cap_count} and no of Small leter is {small_count}"
str1="Write a Function to Count Capital and Small Letters In A StrinG"
print(cap_small(str1))