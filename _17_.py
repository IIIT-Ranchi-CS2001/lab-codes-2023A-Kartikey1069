n=int(input("enter the length : "))
l=[]
k=[]
for i in range(0,n):
    l.append(input("enter the course code: "))
    k.append(input("enter the course name: "))
a=[]
for i in range(0,n):
    a.append(l[i]+":"+k[i])
print(a)    