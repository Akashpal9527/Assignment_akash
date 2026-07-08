# 6. Write a program to separate odd and even keys from a dictionary. Also count the total number of odd keys and even keys.
def separate(d):
    odd={}
    even={}
    count1,count2=0,0
    for i in d:
        if i%2==0:
            even[i]=d.get(i)
            count1+=1
        else:
            odd[i]=d.get(i)
            count2+=1
    return {
        f"odd keys are :{odd}",
        f"even keys are:{even}",
        count1,
        count2
    }
d={1:"akash",2:"arvind",3:"ravi",4:"akashdeep",5:"vivek"}
print(separate(d))