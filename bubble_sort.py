# O(n2)
def bubble_sort(a):
    for i in range(0,len(a)-1):
        print(a)
        for j in range(0,len(a)-i-1):
            # comparing elements i,i+1
            if a[j]>a[j+1]:
                a[j],a[j+1] = (a[j+1],a[j])
    return a

ar = [38,2,1,98,99,8766,887,432,4]
bubble_sort(ar)