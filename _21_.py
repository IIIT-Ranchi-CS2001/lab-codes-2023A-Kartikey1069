k=input("enter the names: ").split()
l1=[i for i in k]
l2=[i for i in map(int,input("enter the roll number:").split())]
l3=[i for i in map(int,input("enter the marks:").split())]
a=[]
for i in range(0,len(l1)):
    k=(l1[i],l2[i],l3[i])
    a.append(k)
a.sort(key=lambda x:x[2])
print(a)    