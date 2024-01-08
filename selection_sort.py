
def selection_sort(a):
    length = len(a)
    for i in range(0,length):

        # finding the minimum value index : mi
        mi = i
        for j in range(i,length):
            if a[mi]>a[j]:
                mi = j
            else:
                pass
        print(a)
        # swapping the minimum and index
        a[i],a[mi] = a[mi],a[i]

    return a

ar = [38,2,1,98,99,8766,887,432,4]
selection_sort(ar)

