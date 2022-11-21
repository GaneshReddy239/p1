l=12
p=[0,1,2,5,6,8,9,10,11]
a=int(input())
if a<len(p):
    print(p[a])
else:
    x=len(p)-1
    while(a>x):
        t=True
        y=str(l)
        for i in y:
            if int(i) not in p:
                t=False
        if t==True:
            p.append(l)
            x+=1
        l=l+1
    print(p[a])
        
        
        
        
        
        
        
    

    
    