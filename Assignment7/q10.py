# 10. Write a function to return the length of a string without using the built-in len() function.
def len_str(str1):
    count=1
    for i in str1:
        if i==" ":
            count+=1
    return f"length of given string is {count}"
str1="Write a function to return the length of a string without using the built-in len() function"
print(len_str(str1))