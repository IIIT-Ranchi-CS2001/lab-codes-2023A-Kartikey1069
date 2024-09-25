t1 = (1,2,3)
t2 = (5,2,6)
tup = tuple(zip(t1,t2))
dist = 0
print(tup)
for i in tup:
    dist = dist + ((i[0] - i[1])**2)
print(dist**0.5)