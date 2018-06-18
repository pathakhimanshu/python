print("enter the number to check armstrong no:")
a=int(input())
b=len(str(a))
c=a
result=0
while(c>0):
    d=c%10
    result+=d**b
    c=c//10


if(result==a):
    print("armstrong no")

else:
    print("not armstrong no")
