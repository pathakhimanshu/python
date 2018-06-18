for item in range(1,10000,1):
    b=len(str(item))
    result=0
    c=item
    while(c>0):
        d=c%10
        result+=(d**b)
        c=c//10
    if(item==result):
        print(result)



    
    
