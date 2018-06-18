print ("enter the number to check palindrome no:")
a=int(input())
c=a
result=0
while(c>0):
    d=c%10
    result=result*10+d
    c=c//10

if(result==a):
    print ("pallindrome no")

else:
    print ("not pallindrome no") 
