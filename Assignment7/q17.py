# 17. Write a function to check if a string is a palindrome or not.
def palindrome(str1):
    s=str1[::-1]
    if str1==s:
        return "Palindrome!"
    else:
        return "Not Palindrome!"
str1="madam"
print(palindrome(str1))
