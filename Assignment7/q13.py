# 13. Write a function to remove all spaces from a given string.
def remove_space(str1):
    new_str=""
    for i  in str1:
        if i!=" ":
            new_str+=i
    return new_str
str1="Write a function to remove all spaces from a given string"
print(remove_space(str1))