def merge(l):
    if len(l)>1:
        mid=len(l)//2
        leftlist=l[:mid]
        rightlist=l[mid:]
        merge(leftlist)
        merge(rightlist)
        i=0;j=0;k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                l[k]=leftlist[i]
                i+=1
                k+=1
            else:
                l[k]=rightlist[j]
                j+=1
                k+=1
        while i<len(leftlist):
            l[k]=leftlist[i]
            k+=1
            i+=1
        while j<len(rightlist):
            l[k]=rightlist[j]
            j+=1
            k+=1
l=[7,5,3,6,2,2]
merge(l)
print(l)
