s=input("enter the sentence:")
t=s.split()
c=0
for i in t:
    if(i==i[::-1]):
        c+=1
print(c)        