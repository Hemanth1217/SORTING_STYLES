l=[7,5,3,6,2,2]
for i in range(len(l)):
    mini=min(l[i:])
    idx=l.index(mini,i)
    l[i],l[idx]=l[idx],l[i]
    print(l)