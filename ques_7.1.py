#question YOu are given with a space sepersted integer list find no of even elements and no of odd elements in a given list


n=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(n)):
    if(n[i]%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)
