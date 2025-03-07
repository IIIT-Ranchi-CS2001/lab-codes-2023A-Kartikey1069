k=input("enter the names: ").split()
l1=[i for i in k]
l2=[i for i in map(int,input("enter the roll number:").split())]
l3=[i for i in map(int,input("enter the marks:").split())]
l=zip(l1,l2,l3)
l=list(l)
print(sorted(l,key=lambda x:x[2]))