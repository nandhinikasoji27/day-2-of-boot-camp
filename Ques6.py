#6. take a space seperator input from user and print alernate elements


a=list(map(int,input().split()))
for i in range(1,n+1,2):
    print(a[i], end=" ")