n=int(input())
f=0
c=1
if(n==1):
    print(f)
elif(n==2):
    print(f)
    print(c)
else:
    print(f)
    print(c)
    while(n-2>0):
        k=f+c
        f=c
        c=k
        print(k)
        n-=1
                