# given an space sepetared int list find the avg of elements present in the even index


n=list(map(int,input().split(" ")))
sum=0
a=len(n)
for i in range(len(n)):
    if(i%2==0):
        sum+=n[i]
print(sum/a)  
             