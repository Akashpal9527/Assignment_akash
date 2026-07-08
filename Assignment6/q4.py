# 4. Create an empty dictionary called user_data. Allow the user to enter key-value pairs until they choose to stop. Print the final dictionary
def dic(key,val,ans):
    d[key]=val
    if ans=="no":
        return d

d={}
while True:
    key=input("enter key:")
    val=input("enter value:")
    choice=input("if you want to continue enter 'yes' else enter 'no'").lower()
    ans=dic(key,val,choice)
    if choice=="no":
        print(ans)
        break
    
