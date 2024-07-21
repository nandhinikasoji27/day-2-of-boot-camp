 
#write a program display 1.append 2.pop,3.sort 4 helo




print("enter the values")
n=list(map(int,input().split()))
print(n)
print("select one option:\n1.append\n2.pop\n3.sort\n4.length")
choice=int(input("enter the choice"))
if(choice==1):
    n.append(int(input("enter any num to append")))
    print(n)
elif(chioce==2):
    n.pop(int(input("enter index number")))
    print(n)
elif(chioce==3):
    n.sort()
    print(n)
else:
    print(len(n))