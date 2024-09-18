s=input("enter the names of singers: ")
s=s.split()
p=input("enter the names of dancers: ")
p=p.split()
dance={i for i in p}
sing={i for i in s}
artist=dance.union(sing)
allrounders=dance.intersection(sing)
dancebutnotsing=artist-sing
singbutnotdance=artist-dance
lastwala=artist-allrounders
print(artist,allrounders,dancebutnotsing,singbutnotdance,lastwala)
