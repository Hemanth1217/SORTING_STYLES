l=[7,5,3,6,2,2]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    print(l)


