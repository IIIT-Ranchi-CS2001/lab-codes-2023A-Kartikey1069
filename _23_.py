dict={}
for i in range(5):
    s=input('enter the name:')
    m=int(input("enter the marks:"))
    dict[s]=m
l1=[]
l2=[]
l3=[]  
m=0  
a=""
for i in dict:   
    if(dict[i]>=85):
        l1.append(i)
        if(dict[i]>=m):
            m=dict[i]
            a=i
    elif(dict[i]>=60):
        l2.append(i) 
    else:
        l3.append(i)
print("high performers: ",len(l1))
print(l1)
print("average performers: ",len(l2))
print(l2)
print("low performers: ",len(l3))
print(l3)
print("highest marks: ",a)               