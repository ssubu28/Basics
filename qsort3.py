# Algorithm - Quick Sort - WORKING (PIVOT = FIRST ELEMENT)

def QuickSort(alist,first,last):
    if first < last:
        # Start only if list has atleast 2 items.
        splitpoint = partition(alist,first,last)
        QuickSort(alist,first,splitpoint-1)       # Left list recursive
        QuickSort(alist,splitpoint+1, last)       # Right list recursive



def partition(alist,first,last):
    i = first + 1                                 # Element after pivot. Since pivot is 0th element.
    j = last
    pivot = alist[first]
    Flag = False

    while not Flag:
        # Individual while loops for finding breaking points
        while i <= j and alist[i] <= pivot:
            i = i + 1

        while j >= i and alist[j] >= pivot:
            j = j - 1

        if i < j:
            # Swap i and j
            alist[i],alist[j] = alist[j],alist[i]

        else:
            # set Flag
            Flag = True

    # Outside iteration: swap j and pivot
    alist[first],alist[j] = alist[j],alist[first]

    # return splitpoint. Used for sub lists creation
    return j



input = raw_input("Enter a list of comma separated values: ").split(',')
alist = [int(i) for i in input]

print alist

QuickSort(alist,0,len(alist)-1)

print alist
