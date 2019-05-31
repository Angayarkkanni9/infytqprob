n=int(input())
c=0
f=True
while(f):
    s=0
    temp=n
    while(n!=0):
        rem=n%10
        s=(s*10)+rem
        n=n//10
    if(s==temp):
        f=False
        break
    else:
        n=int(s)+int(temp)
        temp=int(s)+int(temp)
        c=c+1
print(str(c)+" "+str(temp))
