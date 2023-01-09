# pivot left
def pivot(l,first,last):
    pi=l[first]
    left=first+1
    right=last
    while True:
        while left <=right and l[left]<=pi:
            left += 1
        while left <=  right and l[right] >= pi:
            right -= 1
        if left > right:
            break
        else:
            l[left], l[right] = l[right], l[left]
    l[first], l[right] = l[right], l[first]
    return right
def quick(l,first,last):
    if first<last:
        p=pivot(l,first,last)
        quick(l,first,p-1)
        quick(l,p+1,last)

l=[7,5,3,6,2,2]
quick(l,0,len(l)-1)
print(l)

