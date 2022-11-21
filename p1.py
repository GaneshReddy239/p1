x=int(input("Enter the Number"))
s=""
a=abs(x)
while a>1:
    s=str(a%3)+s
    a=a//3
s=str(a)+s
if x<0:
    s="-"+s
print(s)

