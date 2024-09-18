n=int(input("enter the length:"))
l=[i for i in list(map(int,input().split()))]
print("mean: ",sum(l)/n)
l.sort()
mid=(0+n-1)//2
s=0
if(n%2==0):
    s=l[mid]+l[mid+1]
    s//=2
else:
    s=l[mid]    
print("median: ",s)
cm=1
c=1
a=[0]*(max(l)+1)
for i in l:
    a[i]+=1
p=max(a)
print("mode: \n")    
for i in range(0,max(l)+1):
    if(a[i]==p):
        print(i,end=" ")
print()        
    