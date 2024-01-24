
def selection_sort(a):
    for i in range(0,len(a)):
        mi = i
        for j in range(i,len(a)):
            if a[mi]>a[j]:
                mi = j
        a[i],a[mi] = a[mi],a[i]
    return a

ar = [38,2,1,98,99,8766,887,432,4]
selection_sort(ar)

