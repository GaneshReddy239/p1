s1,s2 = input("Enter two values: ").split(',')
k=s2[-1]
c=0
for i in s1:
    if i==k:
        c+=1
print(c)