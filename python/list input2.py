print "enter the number of elements"
n=input()

a=[]

for i in range(0,n+1,1):
    print"enter the ",i+1,"numer"
    b=input()
    a.insert(i,b)    #list.insert(index,obj)

print(a)
