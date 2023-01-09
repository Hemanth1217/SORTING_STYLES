l=[7,5,3,6,2,2]
for i in range(1,len(l)):
    curr=l[i]
    pos=i
    while pos>0 and curr<l[pos-1]:
        l[pos]=l[pos-1]
        pos=pos-1
    l[pos]=curr
    print(l)